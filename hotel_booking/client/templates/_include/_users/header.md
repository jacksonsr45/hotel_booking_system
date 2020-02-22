{% block header %}
    <header>
        <nav class="navbar navbar-expand-md navbar-light bg-light">
            <a href="/" class="navbar-brand">GNJSistemas</a>
            <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <div class="navbar-nav">
                    <a href="{% url 'home' %}" class="nav-item nav-link active">Home</a>
                    <a href="{% url 'about' %}" class="nav-item nav-link">Sobre</a>
                    <a href="/suas_reservas" class="nav-item nav-link">Suas Reservas</a>
                    <a href="{% url 'contact' %}" class="nav-item nav-link">Contato</a>
                    <a href="" class="nav-item nav-link">País</a>
                    {% if user.is_authenticated %}
                        <li class="nav-item">
                            <a class="nav-item nav-link" href="{% url 'logout' %}">
                            Logout
                            </a>
                        </li>
                    {% else %}
                        <a href="{% url 'validation' %}" class="nav-item nav-link" tabindex="-1">Login</a>
                    {% endif %}
                </div>
            </div>
        </nav>
    </header>
{% endblock %}