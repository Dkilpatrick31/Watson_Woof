console.log('Hello');


$('button').on('click', function(event){
  event.preventDefault();
  var element = $(this);
  $.ajax({
    url: '/like_dog/',
    method: 'GET',
    data: {dog_id: element.attr('data-id')},
    success: function(response){
      element.html('Likes: ' + response);
    }
  })
})
