page('/', authManager.requiresAuthentication, todoManager.listAll);
page('/todo/create', authManager.requiresAuthentication, todoManager.create);
page('/todo/:id', authManager.requiresAuthentication, todoManager.listOne);

page('/login', authManager.showLogin);
page('/logout', authManager.logout);
page('/register', authManager.showRegister);

page({});
