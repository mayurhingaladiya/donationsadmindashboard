<template>
    <div class="chart-container" v-if="isDataAvailable">
        <canvas ref="donationChart"></canvas>
    </div>
    <p v-else>Loading chart data...</p>
</template>

<script>
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
    props: {
        charityData: {
            type: Array,
            required: true,
        },
    },
    computed: {
        isDataAvailable() {
            return this.charityData && this.charityData.length > 0;
        },
    },
    watch: {
        charityData: {
            immediate: true,
            handler() {
                if (this.isDataAvailable) this.renderChart();
            },
        },
    },
    methods: {
        renderChart() {
            if (this.chart) this.chart.destroy();
            const labels = this.charityData.map(item => item.charityName);
            const data = this.charityData.map(item => item.totalAmount);

            this.chart = new Chart(this.$refs.donationChart, {
                type: 'bar',
                data: {
                    labels,
                    datasets: [{
                        label: 'Total Donations per Charity',
                        data,
                        backgroundColor: 'rgba(75, 192, 192, 0.6)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1,
                    }],
                },
                options: {
                    responsive: true,
                    scales: {
                        y: { beginAtZero: true },
                    },
                },
            });
            this.$emit('chart-rendered', { labels, data });
        },
    },
};
</script>
