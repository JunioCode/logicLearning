$('form input[type="file"]').change(event => {
    let arquivos = event.target.files;
    if (arquivos.length === 0 ){
        console.log('sem imagem pra mostrar')
    } else {
        if (arquivos[0].type == 'image/jpeg'){
            $('figure').prepend(imagem);
        } else{
            alert('Formato não suportado')
        }
    }
})