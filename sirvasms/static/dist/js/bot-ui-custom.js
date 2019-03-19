// Pusher Settings =========================================

Pusher.logToConsole = true;
var pusher = new Pusher('b64c6e381c0fde30c2ec', {
  cluster: 'ap1',
  encrypted: true
});
var channel = pusher.subscribe("admin");




// Send Message to Server =========================================

function send_message(message) {

  pusherid = "admin"

  $.ajax({
    url: "https://bot.jobaxy.com/ajax_submit_chat/",
    type: 'GET',
    data: {
      'pusherid': pusherid,
      'message': message
    },
    dataType: 'json',

    success: function(data) {
      console.log(data);
    }
  });
}










// Output Text & Input Email =========================================

channel.bind('output-text-input-email', function(data) {

  botui.message.add({ // show a message
    delay: data.delay,
    loading: data.loading,
    content: data.text
  }).then(function() { // wait till its shown
    return botui.action.text({ // show 'text' action
      action: {
        sub_type: 'email',
        placeholder: 'Your Email..'
      }
    });
  }).then(function(res) { // get the result
    console.log(res.value);
    send_message(res.value)
  });

});

// Output Text & Input Location ==================================

channel.bind('output-text-input-location', function(data) {

  botui.message.add({ // show a message
    delay: data.delay,
    loading: data.loading,
    content: data.text
  }).then(function() { // wait till its shown
    return botui.action.text({ // show 'text' action
      action: {
        size: 30,
        icon: 'map-marker',
        placeholder: 'Location..'
      }
    });
  }).then(function(res) { // get the result
    console.log(res.value);
    send_message(res.value)
  });

});


// Output Text & Input Text =========================================

channel.bind('output-text-input-text', function(data) {

  botui.message.add({ // show a message
    delay: data.delay,
    loading: data.loading,
    content: data.text
  }).then(function() { // wait till its shown
    return botui.action.text({ // show 'text' action
      action: {
        placeholder: 'Write a message..'
      }
    });
  }).then(function(res) { // get the result
    console.log(res.value);
    send_message(res.value)
  });

});



// Output Text & Input Actions =========================================

channel.bind('output-text-input-actions', function(data) {
  
  botui.message.add({ // show a message
    delay: data.delay,
    loading: data.loading,
    content: data.text
  }).then(function() { // wait till its shown
    return botui.action.button({
      
      action: data.actions
      
    }).then(function(res) { // will be called when a button is clicked.
      console.log(res.value);
      send_message(res.value)
    });
  })

});


// Output Video & Input Text =========================================

channel.bind('output-embed-input-text', function(data) {

  botui.message.add({ // show a message
      delay: data.delay,
      loading: data.loading,
      type: 'embed', // this is 'text' by default
      content: data.text
  }).then(function() { // wait till its shown
    return botui.action.text({ // show 'text' action
      action: {
        placeholder: 'Write a message..'
      }
    });
  }).then(function(res) { // get the result
    console.log(res.value);
    send_message(res.value)
  });

});


// Output Link =========================================

channel.bind('output-link', function(data) {

  botui.message.add({
    delay: data.delay,
    loading: data.loading,
    content: data.text
  });
 

});

// Output Link =========================================

channel.bind('output-image', function(data) {

  botui.message.add({
    content: data.text
  });

});


// Output Image & Input Text =========================================

channel.bind('output-image-input-text', function(data) {

  botui.message.add({ // show a message
    delay: data.delay,
    loading: data.loading,
    content: data.text
  });

});













// Output Text & Input Select =========================================

channel.bind('output-text-input-select', function(data) {
  
      botui.message.add({ // show a message
        delay: data.delay,
        loading: data.loading,
        content: data.text
      }).then(function() { // wait till its shown
        return botui.action.select({

      action: {
          placeholder : "Select Experience", 
          value: 'Fresh Graduate',
          searchselect : true,
          label : 'text',
          options: data.actions,
          button: {
            icon: 'check',
            label: 'OK'
          }
        }

      }).then(function (res) { // will be called when a button is clicked.
        console.log(res.value); // will print "one" from 'value'
        send_message(res.value)
      });

    });

});





