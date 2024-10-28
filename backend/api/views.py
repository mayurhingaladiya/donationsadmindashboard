from django.http import JsonResponse
from .models import Contributor, Charity, Donation
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from datetime import datetime
import json


@csrf_exempt
def get_contributors(request):
    """ Return list of contributors """
    if request.method == 'GET':
        contributors = list(Contributor.objects.values())
        return JsonResponse({'contributors': contributors})
    elif request.method == 'POST':
        data = json.loads(request.body)
        contributor = Contributor.objects.create(
            name=data['name'], email=data['email'], member=data['member'])
        return JsonResponse({'id': contributor.id, 'name': contributor.name, 'email': contributor.email, 'member': contributor.member})


def get_charities(request):
    """ Return list of charities """
    if request.method == 'GET':
        charities = list(Charity.objects.values())
        return JsonResponse({'charities': charities})


def get_donations(request):
    """ Return list of donations """
    if request.method == 'GET':
        donations = Donation.objects.select_related('contributor', 'charity').all()
        donation_list = []
        for donation in donations:
            donation_list.append({
                'id': donation.id,
                'contributor_id': donation.contributor.id,
                'contributor_name': donation.contributor.name,
                'charity_id': donation.charity.id,
                'charity_name': donation.charity.name,
                'amount': str(donation.amount),
                'date': donation.date.strftime("%Y-%m-%d"),
            })
        return JsonResponse({'donations': donation_list})
    else:
        return JsonResponse({"error": "Invalid HTTP method."}, status=405)


@csrf_exempt
def add_donation(request):
    """ Add a new donation """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            contributor_id = data.get("contributor_id")
            charity_id = data.get("charity_id")
            amount = data.get("amount")
            date_str = data.get("date")

            if not all([contributor_id, charity_id, amount, date_str]):
                return JsonResponse({"error": "All fields (contributor_id, charity_id, amount, date) are required."}, status=400)

            try:
                contributor = Contributor.objects.get(id=contributor_id)
            except Contributor.DoesNotExist:
                return JsonResponse({"error": "Contributor not found."}, status=404)

            try:
                charity = Charity.objects.get(id=charity_id)
            except Charity.DoesNotExist:
                return JsonResponse({"error": "Charity not found."}, status=404)

            try:
                # Convert to date object
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

            donation = Donation.objects.create(
                contributor=contributor,
                charity=charity,
                amount=amount,
                date=date
            )

            return JsonResponse({
                "id": donation.id,
                "contributor_id": donation.contributor.id,
                "charity_id": donation.charity.id,
                "amount": str(donation.amount),
                "date": donation.date.strftime("%Y-%m-%d")
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
        except Exception as e:
            print(f"Error occurred: {e}")
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)
    else:
        return JsonResponse({"error": "Invalid HTTP method."}, status=405)


@csrf_exempt
def contributor_detail(request, pk):
    """ Edit or delete a contributor """
    try:
        contributor = Contributor.objects.get(pk=pk)
    except Contributor.DoesNotExist:
        return JsonResponse({'error': 'Contributor not found'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        contributor.name = data['name']
        contributor.email = data['email']
        contributor.member = data['member']
        contributor.save()
        return JsonResponse({'id': contributor.id, 'name': contributor.name, 'email': contributor.email, 'member': contributor.member})

    elif request.method == 'DELETE':
        contributor.delete()
        return JsonResponse({'message': 'Contributor deleted successfully'})
