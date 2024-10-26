<template>
    <div class="main-body">
        <h2 id="main-title">Donations Admin Dashboard</h2>
        <ul class="nav nav-tabs" id="dataTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="contributors-tab" data-bs-toggle="tab"
                    data-bs-target="#contributors" type="button" role="tab" aria-controls="contributors"
                    aria-selected="true" @click="fetchContributors">
                    Contributors
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="charities-tab" data-bs-toggle="tab" data-bs-target="#charities"
                    type="button" role="tab" aria-controls="charities" aria-selected="false" @click="fetchCharities">
                    Charities
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="donations-tab" data-bs-toggle="tab" data-bs-target="#donations"
                    type="button" role="tab" aria-controls="donations" aria-selected="false" @click="fetchDonations">
                    Donations
                </button>
            </li>
        </ul>

        <div class="tab-content mt-3" id="dataTabsContent">
            <!-- Contributors Tab -->
            <div class="tab-pane fade show active" id="contributors">
                <h3 class="model-title">Contributors</h3>
                <button class="btn btn-primary mb-3" @click="openContributorModal()">Add Contributor</button>
                <table class="table table-striped" v-if="contributors.length">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="contributor in contributors" :key="contributor.id">
                            <td>{{ contributor.id }}</td>
                            <td>{{ contributor.name }}</td>
                            <td>{{ contributor.email }}</td>
                            <td>
                                <button class="btn btn-sm btn-warning mx-1"
                                    @click="openContributorModal(contributor)">Edit</button>
                                <button class="btn btn-sm btn-danger"
                                    @click="deleteContributor(contributor.id)">Delete</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p v-else>No contributors found.</p>
            </div>
            <!-- Contributor Modal -->
            <div class="modal fade" id="contributorModal" tabindex="-1" aria-labelledby="contributorModalLabel"
                aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">{{ editingContributor ? "Edit Contributor" : "Add Contributor" }}
                            </h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <form @submit.prevent="saveContributor">
                                <div class="mb-3">
                                    <label for="name" class="form-label">Name</label>
                                    <input type="text" class="form-control" v-model="newContributor.name" required />
                                </div>
                                <div class="mb-3">
                                    <label for="email" class="form-label">Email</label>
                                    <input type="email" class="form-control" v-model="newContributor.email" required />
                                </div>
                                <button type="submit" class="btn btn-success">{{ editingContributor ? "Save Changes" :
                                    "Add Contributor" }}</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Charities Tab -->
            <div class="tab-pane fade" id="charities" role="tabpanel" aria-labelledby="charities-tab">
                <h3 class="model-title">Charities</h3>
                <table class="table table-striped" v-if="charities.length">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="charity in charities" :key="charity.id">
                            <td>{{ charity.id }}</td>
                            <td>{{ charity.name }}</td>
                            <td>{{ charity.description }}</td>
                        </tr>
                    </tbody>
                </table>
                <p v-else>No charities found.</p>
            </div>

            <!-- Donations Tab -->
            <div class="tab-pane fade" id="donations" role="tabpanel" aria-labelledby="donations-tab">
                <h3 class="model-title">Donations</h3>
                <button class="btn btn-primary mb-3" data-bs-toggle="modal" data-bs-target="#addDonationModal">
                    Add Donation
                </button>
                <table class="table table-striped" v-if="donations.length">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Contributor Name</th>
                            <th>Charity Name</th>
                            <th>Amount</th>
                            <th>Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="donation in donations" :key="donation.id">
                            <td>{{ donation.id }}</td>
                            <td>{{ donation.contributor_name }}</td> <!-- Updated to show name -->
                            <td>{{ donation.charity_name }}</td> <!-- Updated to show name -->
                            <td>{{ donation.amount }}</td>
                            <td>{{ donation.date }}</td>
                        </tr>
                    </tbody>
                </table>
                <p v-else>No donations found.</p>
            </div>
        </div>

        <!-- Add Donation Modal -->
        <div class="modal fade" id="addDonationModal" tabindex="-1" aria-labelledby="addDonationModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addDonationModalLabel">Add Donation</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="addDonation">
                            <div class="mb-3">
                                <label for="contributor" class="form-label">Contributor</label>
                                <select v-model="newDonation.contributor_id" class="form-select" required>
                                    <option v-for="contributor in contributors" :key="contributor.id"
                                        :value="contributor.id">
                                        {{ contributor.name }}
                                    </option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label for="charity" class="form-label">Charity</label>
                                <select v-model="newDonation.charity_id" class="form-select" required>
                                    <option v-for="charity in charities" :key="charity.id" :value="charity.id">
                                        {{ charity.name }}
                                    </option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label for="amount" class="form-label">Amount</label>
                                <input type="number" v-model="newDonation.amount" class="form-control" required />
                            </div>
                            <div class="mb-3">
                                <label for="date" class="form-label">Date</label>
                                <input type="date" v-model="newDonation.date" class="form-control" required />
                            </div>
                            <button type="submit" class="btn btn-success">Save Donation</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div>
            <DonationChart :charityData="charityDonationData" />

        </div>
    </div>
</template>

<script>
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';
import DonationChart from './components/DonationChart.vue';

export default {
    components: {
        DonationChart,
    },
    data() {
        return {
            contributors: [],
            charities: [],
            donations: [],
            newDonation: {
                contributor_id: null,
                charity_id: null,
                amount: '',
                date: ''
            },
            newContributor: { name: '', email: '' },
            editingContributor: null,
            charityDonationData: [],
        };
    },
    methods: {
        // Fetch data methods
        fetchContributors() {
            fetch('http://127.0.0.1:8000/api/contributor/')
                .then(response => response.json())
                .then(data => { this.contributors = data.contributors; })
                .catch(error => console.error("Error fetching contributors:", error));
        },

        fetchCharities() {
            fetch('http://127.0.0.1:8000/api/charities/')
                .then(response => response.json())
                .then(data => { this.charities = data.charities; })
                .catch(error => console.error("Error fetching charities:", error));
        },

        fetchDonations() {
            fetch('http://127.0.0.1:8000/api/donations/')
                .then(response => response.json())
                .then(data => { this.donations = data.donations; this.calculateCharityTotals(); })
                .catch(error => console.error("Error fetching donations:", error));
        },

        addDonation() {
            fetch('http://127.0.0.1:8000/api/donations/add/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newDonation)
            })
                .then(response => {
                    if (!response.ok) {
                        return response.json().then(errorData => {
                            throw new Error(errorData.error);
                        });
                    }
                    return response.json();
                })
                .then(data => {
                    this.donations.push(data);
                    this.newDonation = { contributor_id: null, charity_id: null, amount: '', date: '' };

                })
                .catch(error => console.error("Error adding donation:", error.message));
        },

        openContributorModal(contributor = null) {
            this.editingContributor = contributor;
            if (contributor) {
                this.newContributor = { ...contributor };
            } else {
                this.newContributor = { name: '', email: '' };
            }
            const modal = new bootstrap.Modal(document.getElementById('contributorModal'));
            modal.show();
        },

        saveContributor() {
            const method = this.editingContributor ? 'PUT' : 'POST';
            const url = this.editingContributor
                ? `http://127.0.0.1:8000/api/contributor/${this.editingContributor.id}/`
                : 'http://127.0.0.1:8000/api/contributor/';

            fetch(url, {
                method: method,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newContributor)
            })
                .then(response => response.json())
                .then(data => {
                    if (this.editingContributor) {
                        const index = this.contributors.findIndex(c => c.id === this.editingContributor.id);
                        this.contributors[index] = data;
                    } else {
                        this.contributors.push(data);
                    }
                    this.editingContributor = null;
                    this.newContributor = { name: '', email: '' };
                    const modal = bootstrap.Modal.getInstance(document.getElementById('contributorModal'));
                    if (modal) modal.hide();
                })
                .catch(error => console.error("Error saving contributor:", error));
        },

        deleteContributor(contributorId) {
            fetch(`http://127.0.0.1:8000/api/contributor/${contributorId}/`, {
                method: 'DELETE',
            })
                .then(() => {
                    this.contributors = this.contributors.filter(c => c.id !== contributorId);
                })
                .catch(error => console.error("Error deleting contributor:", error));
        },

        calculateCharityTotals() {
            const charityLookup = this.charities.reduce((acc, charity) => {
                acc[charity.id] = charity.name;
                return acc;
            }, {});

            const totals = this.donations.reduce((acc, donation) => {
                const charityId = donation.charity_id;
                const charityName = charityLookup[charityId] || 'Unknown Charity';

                if (!acc[charityId]) {
                    acc[charityId] = { charityName: charityName, totalAmount: 0 };
                }
                acc[charityId].totalAmount += parseFloat(donation.amount);
                return acc;
            }, {});

            this.charityDonationData = Object.values(totals);
        }
    },
    mounted() {
        this.fetchContributors();
        this.fetchCharities();
        this.fetchDonations();
    },
};
</script>

<style scoped>
.main-body {
    padding: 20px;
    font-family: 'Merriweather', serif;
    margin-inline: 100px;

}

#main-title {
    font-size: 2.5rem;
    text-align: center;
    margin: 0;
    padding: 20px;
    background-color: #007bff;
    color: white;
    border-radius: 8px;
    margin-bottom: 20px;
}

.model-title {
    background-color: #FFC107;
    border-radius: 8px;
    padding: 10px;
    width: fit-content;
}

.tab-content {
    margin-top: 20px;
}

.table {
    margin-top: 10px;
}
</style>
