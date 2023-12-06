 // Function para carregar todos os Feed
// window.addEventListener('load', function () {
//     const feedlist = document.getElementById('feed-list')
//     // alert('hello word!')
//     fetch('http://127.0.0.1:8000/api/feeds/')
//     .then((resp) => resp.json())
//     .then((data) => {
//         // console.log(data)
//         // console.log(resp)
//        const feeds = data.map(feed => {
//         const listitem = document.createElement('div')
//         listitem.className = 'feed-list'
//         listitem.innerHTML = `
//             <h2>${feed.plataforma.nome}</h2>
//             <h3>${feed.ouvidoria.nome}</h3>
//             <p>${feed.mensagem_digitada_na_ouvidoria}</p>`
//         return listitem
//         })
//         feeds.forEach(list => {
//             feedlist.appendChild(list)
//         })
//     })
// })


// Função para carregar as plataformas
window.addEventListener('load', function () {
    fetch('http://localhost:8000/api/plataformas/')
    .then((resp) => resp.json())
    .then(resp => {
        // console.log(resp)
        const select = document.querySelector('#select_Plataform')

        resp.forEach(plataform => {
            const opt = document.createElement('option')
            opt.value = plataform.id
            opt.textContent = plataform.nome
            select.appendChild(opt)
        })
    })
})

window.addEventListener('load', function () {
    fetch('http://localhost:8000/api/ouvidorias/')
    .then((resp) => resp.json())
    .then(resp => {
        // console.log(resp)
        const radio = document.querySelector('#select_Ouvidoria')

        resp.forEach(ouvidoria => {
            const radio = document.createElement('input')
            const label = document.querySelector('#select_Ouvidoria')
            radio.type = 'radio'
            radio.name = 'Ouvidoria'
            radio.value = ouvidoria.id

            label.appendChild(radio)
            label.appendChild(document.createTextNode(` ${ouvidoria.nome}`))

            
        })
    })
})

