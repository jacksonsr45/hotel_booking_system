{% block content %}
    {% if user.username %}
        {{ user.username }}
    {% endif %}
{% endblock %}