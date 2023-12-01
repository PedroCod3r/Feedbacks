function render_element (plataforma, ouvidoria, mensagem) {
    return `
    <div class="plataform-feeds">
    
        <div class= "container-plataforma"> 
            <h2>Plataforma: ${plataforma}</h2>
        </div>
        <div class = "container-ouvidoria">
            <h2>Ouvidoria: ${ouvidoria}</h2>
        </div>

        <div class = "container-mensagem">
            <p>Mensagem Digitada: ${mensagem}</p>
        </div>

    </div>`
}

function render_feedback() {
    fetch('http://127.0.0.1:8000/api/feeds/')
    .then((resp) => resp.json())
    .then((resp) => {
        const feeds = resp.map(feed => render_element(feed.plataforma, feed.ouvidoria, feed.mensagem))
        document.getElementById('feed-list').innerHTML = feeds.join()
    })
}