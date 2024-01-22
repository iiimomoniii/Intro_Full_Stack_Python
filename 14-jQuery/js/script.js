//click on h1 in html will show There was a click! on Console of browser
$('h1').click(function(){
    console.log('There was a click!');
});

$('li').click(function(){
    console.log('any li was clicked!');
})

$('#changeTitle').click(function(){
    $(this).text("I was changed!");
})

//Key press
$('input').on("keypress",function(event){
    if (event.which == 13){
        console.log(event);
        $('h1').toggleClass('turnBlue');
    }
    $('h3').toggleClass('turnBlue');
})

//on()
$().on('dbclick',function(){
    $(this).toggleClass('turnBlue')
})

//slideup
$('input').on('click',function(){
    $('.container').slideUp(3000);
})