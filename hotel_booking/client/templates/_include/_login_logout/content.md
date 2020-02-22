{% block content %}
    <div class="container-fluid login p-5">
        <div class="container">
            <div class="d-flex justify-content-center h-100">
                <div class="card">
                    <div class="card-header">
                        <h3>Login</h3>
                        <div class="d-flex justify-content-end social_icon">
                            <span><i class="fab fa-facebook-square"></i></span>
                            <span><i class="fab fa-google-plus-square"></i></span>
                            <span><i class="fab fa-twitter-square"></i></span>
                        </div>
                    </div>
                    <div class="card-body">
                        <form method="post" action="{% url 'login' %}">
                            {% csrf_token %}
                            <div class="input-group form-group">
                                <div class="input-group-prepend">
                                    <span class="input-group-text"><i class="fas fa-user"></i></span>
                                </div>
                                <input type="username" class="form-control" name="username" id="username" placeholder="username">						
                            </div>
                            <div class="input-group form-group">
                                <div class="input-group-prepend">
                                    <span class="input-group-text"><i class="fas fa-key"></i></span>
                                </div>
                                <input type="password" class="form-control" name="password" id="password" placeholder="password">
                            </div>
                            <div class="form-group">
                                <button type="submit" class="btn float-right login_btn" value="login">Login</button>
                            </div>
                        </form>
                    </div>
                    <div class="card-footer">
                        <div class="d-flex justify-content-center links">
                            Ainda não tem uma conta?
                            <a href="#">Criar nova conta</a>
                        </div>
                        <div class="d-flex justify-content-center">
                            <a href="#">Esqueceu sua senha?</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}