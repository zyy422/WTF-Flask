let dom = document.getElementById("container");
let myChart = echarts.init(dom);
let app = {};
option = null;
option = {
    title: {
        text: 'Data Visualization Assistant'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['Exhaust（normal temperature）','Exhaust(150℃)','Leak rate','mean value']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['周一','周二','周三','周四','周五','周六','周日']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'Exhaust（normal temperature）',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'Exhaust(150℃)',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'Leak rate',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'mean value',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        }
    ]
};
if (option && typeof option === "object")
{
    myChart.setOption(option, true);
}

