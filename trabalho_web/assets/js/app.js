document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('.menu-princ-item');
    const content = document.getElementById('content');

    // Carregar conteúdo ao clicar nos links
    links.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const sectionId = this.getAttribute('href').substring(1);
            loadSection(sectionId);
        });
    });

    // Função para carregar a seção
    function loadSection(sectionId) {
        let sectionContent = '';

        switch (sectionId) {
            case 'sobre':
                sectionContent = `
                <section id="sobre">
                <h1>Sobre Mim</h1>
                <p>Olá! Meu nome é Valeska, sou uma pessoa apaixonada por várias coisas na vida. Primeiramente, sou costureira, profissão na qual me realizo criando e transformando tecidos em peças únicas e cheias de personalidade. Além disso, sou estudante de Análise e Desenvolvimento de Sistemas (ADS), onde estou explorando o fascinante mundo da tecnologia e programação.</p>
                    
                    <p>Sou mãe de uma bebê linda chamada Ariella, que enche meus dias de alegria e amor. Já moro em Portugal há 4 anos e, neste tempo, criei raízes e uma conexão especial com este país. Além de mãe e estudante, sou também noiva do Mathias, que sempre brinca dizendo que sou uma nerd — e não posso negar, adoro aprender e mergulhar em novos conhecimentos!</p>
                    
                    <p>Quando não estou me dedicando à minha profissão ou aos estudos, você pode me encontrar assistindo meus animes favoritos, outra paixão que cultivo há anos. Também adoro viajar e descobrir novos lugares, culturas e sabores. E, claro, não posso deixar de mencionar meu amor por tatuagens, que representam um pouco de quem sou e das minhas experiências ao longo da vida.</p>
                    
                    <p>Essa é um pouco da minha história e do que me move. Estou sempre buscando novos desafios e aprendizados, tanto na costura quanto na tecnologia, e mal posso esperar para compartilhar mais do meu trabalho e das minhas paixões com você!</p>
            </section>`;
                break;
            case 'formacao':
                sectionContent = `
                <section id="formacao">
                <h1>Formação</h1>
                <ul>
                    <li><h2>Formação Educacional</h2></li>
                    <li>Ensino médio completo.</li>
                    <li>Ensino Superior: Cursando</li>
                    <li><h2>Idiomas</h2></li>
                    <li>Inglês</li>
                    <li>Espanhol</li>
                </ul>
            </section>`;
                break;
            case 'projeto':
                sectionContent = `
                <section id="projeto"> 
                <h1>Projetos</h1>
                <a id="link-meugit"  href="https://github.com/ValeskaCarvalho1/projetos_faculdade">🥰Meu github</a>
            </section>`;
                break;
            case 'contato':
                sectionContent = `
                <section id="contato">
                <h1>Contato</h1>
                <p>Preencha o formulário abaixo para entrar em contato comigo:</p>
                <div class="form-container">
                <form action="#" method="post">
                <!-- Campo para o nome -->
                <label for="name">Nome:</label>
                <input type="text" id="name" name="name" required>
    
                <!-- Campo para o e-mail -->
                <label for="email">E-mail:</label>
                <input type="email" id="email" name="email" required>
    
                <!-- Campo para a mensagem -->
                <label for="message">Mensagem:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
    
                <!-- Botão de envio -->
                <input type="submit" value="Enviar">
            </form>
                </div>
                
            </section>
        </div>`;
                break;
            default:
                sectionContent = '<section><h1>Página não encontrada</h1></section>';
        }

        content.innerHTML = sectionContent;
    }
});
