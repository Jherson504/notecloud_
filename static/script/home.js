const nav_tab = document.getElementById("nav-tab");
const nav_tabContent = document.getElementById('nav-tabContent');
const main = document.getElementById("primary-container");
const explore = document.getElementById('nav-explore-content');
const activities = document.getElementById('nav-activities-content');


var activeTab = explore;


window.addEventListener('resize', checkForResize)


function checkForResize() {
    
    
    if (window.innerWidth >= 992) {
        activities.classList.add('active', 'show');
        explore.classList.add('active', 'show');
    }
    else {
        activities.classList.remove('active', 'show');
    }
}


checkForResize();