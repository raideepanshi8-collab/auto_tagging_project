const API = "http://localhost:5000/api";

async function load(){
  const res = await fetch(API+"/papers/mypapers",{
    headers:{Authorization:localStorage.getItem("token")}
  });

  const data = await res.json();

  let count = {};

  data.forEach(p=>{
    p.tags.forEach(t=>{
      count[t] = (count[t]||0)+1;
    });
  });

  new Chart(document.getElementById("chart"),{
    type:"bar",
    data:{
      labels:Object.keys(count),
      datasets:[{data:Object.values(count)}]
    }
  });
}

load();