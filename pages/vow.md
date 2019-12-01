---
layout: page
title: "The RSE Manifesto: Vow"
permalink: /vow/
---

<!-- Page Content -->
<div class="container">
  <div class="row">
      <h5>As a Research Software Engineer:</h5>
      <div id="vow-text">
      </div>
  </div>
</div>
<script>

// populate page with all vows
vows = { {% for vow in site.data.manifesto %}"{{ vow.name }}": {"vow": "{{ vow.vow }}"} {% if forloop.last %}{% else %},{% endif %}{% endfor %}}
console.log(vows)
function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

var vow = getUrlVars()["q"];
vow = decodeURI(vow);

if (vow in vows) {
  console.log(vow)
  document.getElementById('page-title').innerHTML = vow;
  document.getElementById('vow-text').innerHTML = vows[vow]["vow"];
} else {
  document.getElementById('vow-text').innerHTML = "We couldn't find the vow " + vow + " in our manifesto. Perhaps you can contribute it?";
}
</script>
