const techincal = document.getElementById('technical');
const social = document.getElementById('social');
const academics = document.getElementById('academics');
const sports = document.getElementById('sports');
const home = document.getElementById('home');

var asd = JSON.parse($('#student0').attr("data_student"));
var company = $('#student5').attr("data_student");
var meanf2 = JSON.parse($('#student6').attr("data_student"));
var maxf2 = JSON.parse($('#student7').attr("data_student"));
var scatter =  JSON.parse($('#student8').attr("data_student"));

console.log(asd);

function activate(e) {
  if (techincal.classList.contains("active")) {
    techincal.classList.remove('active');
    e.target.classList.add('active');
  } else if (sports.classList.contains('active')) {
    sports.classList.remove('active');
    e.target.classList.add('active');
  } else if (social.classList.contains('active')) {
    social.classList.remove('active');
    e.target.classList.add('active');
  } else if (academics.classList.contains('active')) {
    academics.classList.remove('active');
    e.target.classList.add('active');
  } else if (home.classList.contains('active')) {
    home.classList.remove('active');
    e.target.classList.add('active');
  }
}

techincal.addEventListener('click', activate);
social.addEventListener('click', activate);
academics.addEventListener('click', activate);
sports.addEventListener('click', activate);
home.addEventListener('click', activate);

// academics

// scattering
const user_tenth_marks = asd[0];
const user_twelth_marks = asd[1];
const trace1 = {
  x: [user_tenth_marks],
  y: [user_twelth_marks],
  mode: 'markers',
  type: 'scatter',
};

const arr1 = scatter[0];
const arr2 = scatter[1];

const trace2 = {
  x: arr1,
  y: arr2,
  mode: 'markers',
  type: 'scatter',
};

const data1 = [trace1, trace2];

Plotly.newPlot('academics-1', data1);

// scattering

// bar

const min_cgpa = 8.5;
const max_cgpa = 9.3;
const user_cgpa = 8.3;

const tracecurr = {
  x: ['Mean', 'Curr', 'Max'],
  y: [min_cgpa, user_cgpa, max_cgpa],
  name: 'CGPA',
  type: 'bar',
  marker: {
    color: ['rgb(255, 180, 155)', 'rgb(237, 104, 151)', 'rgb(255, 180, 155)'],
  }
};

const data2 = [tracecurr];

Plotly.newPlot('academics-2', data2);

// bar

// academics

// sports

// bar

const min_sports_eq = 6;
const max_sports_eq = 7;
const user_sports_eq = 3;

const tracecurr1 = {
  x: ['Mean', 'Curr', 'Max'],
  y: [min_sports_eq, user_sports_eq, max_sports_eq],
  marker:  {
    color: ['rgb(255, 180, 155)', 'rgb(237, 104, 151)', 'rgb(255, 180, 155)'],
  },
  name: 'Sports',
  type: 'bar',
};

const data3 = [tracecurr1];

Plotly.newPlot('sports-1', data3);

// bar

// sports

// technical

// scattering

const user_hackathon = asd[3];
const user_internship = asd[5];
const trace3 = {
  x: [user_hackathon],
  y: [user_internship],
  mode: 'markers',
  type: 'scatter',
};

const arr3 = scatter[2];
const arr4 = scatter[3];

const trace4 = {
  x: arr3,
  y: arr4,
  mode: 'markers',
  type: 'scatter',
};

const data4 = [trace3, trace4];

Plotly.newPlot('technical-1', data4);

// scattering

// line

const user_projects = asd[6];
const trace8 = {
  x: [user_hackathon],
  y: [user_projects],
  mode: 'markers',
  type: 'scatter',
};

const arr5 = scatter[2];
const arr6 = scatter[4];

const trace9 = {
  x: arr5,
  y: arr6,
  mode: 'markers',
  type: 'scatter',
};

const data5 = [trace8, trace9];

Plotly.newPlot('technical-2', data5);

// line

// bar

const min_no_of_research_papers = meanf2[3];
const max_no_of_research_papers = maxf2[3];
const user_no_of_research_papers = asd[4];

const tracecurr2 = {
  x: ['Mean', 'Curr', 'Max'],
  y: [
    min_no_of_research_papers,
    user_no_of_research_papers,
    max_no_of_research_papers,
  ],
  marker:  {
    color: ['rgb(255, 180, 155)', 'rgb(237, 104, 151)', 'rgb(255, 180, 155)'],
  },
  name: 'Research Papers',
  type: 'bar',
};

const data6 = [tracecurr2];

Plotly.newPlot('technical-3', data6);

// bar

// technical

// social

const min_no_of_hours = meanf2[2];
const max_no_of_hours = maxf2[2];
const user_no_of_hours = asd[7];

const tracecurr3 = {
  x: ['Mean', 'Curr', 'Max'],
  y: [min_no_of_hours, user_no_of_hours, max_no_of_hours],
  name: 'Social Work',
  type: 'bar',
  marker:  {
    color: ['rgb(255, 180, 155)', 'rgb(237, 104, 151)', 'rgb(255, 180, 155)'],
  }
};

const data7 = [tracecurr3];

Plotly.newPlot('social-1', data7);

// social
