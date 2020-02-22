{% block content %}
    <form method="post" action="{% url 'login' %}">
        {% csrf_token %}
        <table>
            <tr>
                <td><label for="Username">Username</label></td>
                <td><input type="username" name="username" id="username"></td>
            </tr>
            <tr>
                <td><label for="Password">Password</label></td>
                <td><input type="password" name="password" id="password"></td>
            </tr>
        </table>
        <button type="submit" value="login">Login</button>
    </form>
{% endblock %}