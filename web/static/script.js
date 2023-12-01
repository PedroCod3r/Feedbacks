// window.addEventListener('load', function () {
//     const feedlist = document.getElementById('feed-list')
//     // alert('hello word!')
//     fetch('http://127.0.0.1:8000/api/feeds/')
//     .then((resp) => resp.json())
//     .then((data) => {
//         // console.log(resp)
//         const feeds = data.map(feed => {
//             const listitem = document.createElement('div')
//             listitem.className = 'feed-list'
//             listitem.textContent = `${feed.mensagem_digitada_na_ouvidoria} - ${feed.plataforma.nome}, ${feed.ouvidoria.nome}`
//             return listitem
//         })
        
//         feeds.forEach(list => {
//             feedlist.appendChild(list)
//         })

//     })
// })

window.addEventListener('load', function () {
    const feedlist = document.getElementById('feed-list')
    // alert('hello word!')
    fetch('http://127.0.0.1:8000/api/feeds/')
    .then((resp) => resp.json())
    .then((data) => {
        console.log(data)
        // console.log(resp)
       const feeds = data.map(feed => {
        const listitem = document.createElement('div')
        listitem.className = 'feed-list'
        listitem.innerHTML = `
            <h2>${feed.plataforma.nome}</h2>
            <h3>${feed.ouvidoria.nome}</h3>
            <p>${feed.mensagem_digitada_na_ouvidoria}</p>`
        return listitem
        })
        feeds.forEach(list => {
            feedlist.appendChild(list)
        })
    })
})

// function render_feedback () {
//     fetch('http://127.0.0.1:8000/api/feeds/')
//     .then((resp) => resp.json())
//     .then((resp) => {
//         const feeds = resp.map(feed => render_element(feed.plataforma, feed.ouvidoria, feed.mensagem))
//         document.getElementById('feed-list').innerHTML = feeds.join()
//     })
// }