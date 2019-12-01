---
layout: default
permalink: /
---

<div class="larg">{% assign vows = site.data.manifesto | sort: 'name' %}
  <dl>{% for vow in vows %}<dt data-dfn="{{ vow.vow }}">{{ vow.name }}</dt>{% endfor %}
  </dl>
</div>
<div class="flap">
</div>
