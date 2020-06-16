//let DemoAvatars = {
//      Avatars: [
//                {'id': 1, 'margin_top': 100, 'habilitar_texto': true, 'titulo': '1/12', 'img': '/static/assets/portal/enquete/enquete.jpeg', 'texto':'O que é Lorem Ipsum dbyqw gwe e we?'},
//                {'id': 2, 'margin_top': 100, 'habilitar_texto': true, 'titulo': '2/12', 'img': '/static/assets/portal/enquete/enquete.jpeg', 'texto':'O que é Lorem Ipsum dbyqw gwe e we?'}
//                ],
//      Modals: {}
//};

let DemoAvatars = { Avatars: [], Modals: {} };

$.get(`../../../../../../CORE_AJAX_ENQUETES`, function( data ) {
    $.each(data['enquetes'], function (index, item) { DemoAvatars['Avatars'].push(item); });
    if (DemoAvatars['Avatars'].length != 0) generateAvatarJBox(true);
});


function generateAvatarJBox(initial) {
  // We only need to initialize the tooltips for the avatar collection once
  // We can later refer to this jBox instance with DemoAvatars.AvatarsTooltip

  !DemoAvatars.AvatarsTooltip && (DemoAvatars.AvatarsTooltip = new jBox('Tooltip', {
    theme: 'TooltipBorder', // We are using the border theme...
    addClass: 'AvatarsTooltip', // ...and add a class so we can adjust the theme with CSS
    attach: '[data-avatar-tooltip]', // We attach the tooltip to the elements with the attribute data-avatar-tooltip...
    getContent: 'data-avatar-tooltip', // ... and also get the content from the same attribute
    zIndex: 12000, // These tooltips have the highest z-index
    animation: 'move',

    // Adding the liked or disliked class depending on the container the avatar is in
    onOpen: function () {
      this.wrapper.removeClass('AvatarsTooltipLike AvatarsTooltipDislike').addClass('AvatarsTooltip' + (this.source.parent().attr('id') == 'LikedAvatars' ? 'Like' : 'Dislike'));
    }
  }));

  // When we are creating the initial jBox, reset global variables

  if (initial) {
    DemoAvatars.clicked = false;
    DemoAvatars.current = -1;
  }

  // Increase current avatar index

  DemoAvatars.current++;

  // When we looped through all the avatars, show a jBox Modal with a hint that there are no more avatars nearby

  if (DemoAvatars.current >= DemoAvatars.Avatars.length) {

    DemoAvatars.Modals.AvatarsComplete = new jBox('Modal', {

      // We use similar options to our Avatar modal so they look similar
      id: 'AvatarsComplete',
      addClass: 'AvatarsModal',
      width: 400,
      height: 400,
      animation: 'zoomIn',
      overlay: false,
      blockScroll: false,
      closeButton: false,
      closeOnEsc: false,
      adjustDistance: {
        top: 40,
        right: 5,
        bottom: 55,
        left: 5
      },
      footer: '<button class="button-close">Fechar</button>',
      title: 'Resultado',
      content: "<div id='resultadoEnquete' style='margin: -150px 0px 0px 0px;'></div>",
      zIndex: 10000,

      // Once this jBox is created, we tel the close button to close the initial avatar modal
      onCreated: function () {
        this.footer.find('button').on('click', function () {
          DemoAvatars.Modals.AvatarsInitial.close();
        });
        $.get('CORE_AJAX_RESULTADO_ENQUETES', function( data ) {
            console.log(data);
            let content_resultado = '';
            $.each(data['resultados'], function (index, item) {
                let SIM = '';
                let NAO = '';
                let barras = '';
                let enquete = item['enquete'];
                $.each(item['respostas'], function (index, item) {
                    let titulo = item.resposta;
                    let valor = item.porcentagem;
                    let cor = item.cor;
                    if(titulo == "SIM") SIM = valor;
                    if(titulo == "NÃO") NAO = valor;

                    barras = barras + `
                        <div class="progress-bar ${cor}" role="progressbar" style="width: ${valor}%;" aria-valuenow="${valor}" aria-valuemin="0" aria-valuemax="100"></div>
                    `
                });
                content_resultado = content_resultado + `
                    <div class="resultadoEnquete">
                        <div><p>${enquete}</p></div>
                        <div class="progress" style="height: 20px; margin: -20px 0px 10px 0px;">${barras}</div>
                        <a href="#" class="button button-small button-circle button-green"><i class="icon-like"></i>SIM ${SIM}% </a>
                        <a href="#" class="button button-small button-circle button-red"><i class="icon-line2-dislike"></i>NÃO ${NAO}%</a>
                    </div>
                `
            });

            $("#resultadoEnquete").html(content_resultado);
        });
      }

    }).open();

    // Nothing more to do, abort here
    return null;
  }

  // We are creating a new jBox Modal with the avatars each time this function gets called

  var jBoxAvatar = new jBox('Modal', {
    addClass: 'AvatarsModal',
    width: 400,
    height: 390,
    animation: 'zoomIn',
    zIndex: 10000,

    // Adjusting the distance to the viewport so we have space for the avatar collection at the bottom and the close button of the modal at the top
    adjustDistance: {
      top: 40,
      right: 5,
      bottom: 55,
      left: 5
    },

    // We are setting these options differently for the initial and the following jBoxes
    id: initial ? 'AvatarsInitial' : 'AvatarsModal' + DemoAvatars.current,
    overlay: initial ? true : false, // Only one overlay is needed
    blockScroll: initial ? true : false, // The initial jBox will block scrolling, no need for the others to o the same
    closeButton: initial ? 'overlay' : false, // The initial jBox will have the close button in the overlay, the others won't need one
    closeOnEsc: initial ? true : false, // Only the inital jBox can be closed with [ESC] button

    // Placing the buttons in the footer area
//    footer: '<button class="button-cross cross"></button><button class="button-heart heart"></button>',
    footer: '<button class="button-cross cross">NÃO</button><button class="button-heart heart">SIM</button>',

    // Open this jBox when it is being initialized
    onInit: function () {
      this.open();

      // Here we store the index we used for this jBox
      this.AvatarIndex = DemoAvatars.current;
    },

    // When the jBox is created, add the click events to the buttons
    onCreated: function () {

      // Create the containers for the liked or disliked avatars
      if (initial) {
        $('<div id="LikedAvatars" class="AvatarsCollection"/>').appendTo($('body'));
        $('<div id="DislikedAvatars" class="AvatarsCollection"/>').appendTo($('body'));
      }

      $.each(this.footer.find('button'), function (index, el) {

        // Adding the click events for the buttons in the footer
        $(el).on('click', function () {


          // Storing a global var that the user clicked on a button
          DemoAvatars.clicked = true;

          // When a user clicks a button close the tooltips
          DemoAvatars.AvatarsTooltipLike && DemoAvatars.AvatarsTooltipLike.close();
          DemoAvatars.AvatarsTooltipDislike && DemoAvatars.AvatarsTooltipDislike.close();

          // When we click a button, the jBox disappears, let's tell this jBox that we removed it
          this.AvatarRemoved = true;

          // Did we like or dislike the avatar?
          var liked = $(el).hasClass('button-heart');

            let id = DemoAvatars.Avatars[DemoAvatars.current]['id'];

            $.get(`../../../../../../../CORE_AJAX_COMPUTAR_VOTO?id=${id}&voto=${liked}`, function( data ) {
                console.log(data)
            });


          // Slide the jBox to the left or right depending on which button the user clicked
          this.animate('slide' + (liked ? 'Right' : 'Left'), {

            // Once the jBox is removed, hide it and show the avatar in the collection
            complete: function () {
              this.wrapper.css('display', 'none');

              // Which container to use
              var collectionContainer = liked ? $('#LikedAvatars') : $('#DislikedAvatars');

              // If there if not enough space for the avatars to show in one line remove the first one
              if (collectionContainer.find('div[data-avatar-tooltip]').length && ((collectionContainer.find('div[data-avatar-tooltip]').length + 1) * $(collectionContainer.find('div[data-avatar-tooltip]')[0]).outerWidth(true) > collectionContainer.outerWidth())) {
                $(collectionContainer.find('div[data-avatar-tooltip]')[0]).remove();
              }

            }.bind(this)
          });

          // Open another Avatar jBox
          generateAvatarJBox();

        }.bind(this));
      }.bind(this));
    },

    // When we open the jBox, set the new content and show the tooltips if it's the initial jBox
    onOpen: function () {

      // Set title and content depending on current index
      let enquete = DemoAvatars.Avatars[DemoAvatars.current];
      let titulo = enquete['titulo'];
      let img = enquete['img'];
      let texto = enquete['texto'];
      let habilitar_texto = enquete['habilitar_texto'];
      let margin_top = 38 + enquete['margin_top'];
      this.setTitle(titulo);
      this.content.css({
        backgroundImage: `url(${img})`,
        backgroundSize: '400px 400px',
      });

      if(habilitar_texto == true) this.setContent(`<div class="enquete-box-texto" style="margin-top: ${margin_top}px !important;"><p> ${texto} </h2></p>`);

      // If it's the inital jBox, show the tooltips after a short delay
      initial && setTimeout(function () {

        // We are creating the two tooltips in a loop as they are very similar
        $.each(['Dislike', 'Like'], function (index, item) {

//          // We store the tooltips in the global var so we can refer to them later
//          DemoAvatars['AvatarsTooltip' + item] = new jBox('Tooltip', {
//            theme: 'TooltipBorder',
//            addClass: 'AvatarsTooltip AvatarsTooltip' + item,
//            minWidth: 110,
//            content: item,
//            position: {
//              y: 'bottom'
//            },
//            offset: {
//              y: 5
//            },
//            target: '#AvatarsInitial .jBox-footer .button-' + (item == 'Like' ? 'heart' : 'cross'),
//            animation: 'move',
//            zIndex: 11000,
//
//            // Abort opening the tooltips when we clicked on a like or dislike button already
//            onOpen: function () {
//              DemoAvatars.clicked && this.close();
//            }
//          }).open();

        });

      }, 500);
    }
  });

  // If it's the inital jBox add onClose events
  initial && (jBoxAvatar.options.onClose = function () {
    // Loop through all avatar jBoxes and close them if they are not removed yet
    $.each(DemoAvatars.Modals, function (index, jBox) {
      jBox.id != 'AvatarsInitial' && !jBox.AvatarRemoved && jBox.close();
    }.bind(this));

    // Remove the collection containers with a sliding animation
    $.each(['Liked', 'Disliked'], function (index, item) {
      this.animate('slide' + (item == 'Liked' ? 'Right' : 'Left'), {
        element: $('#' + item + 'Avatars'),
        complete: function () {
          $('#' + item + 'Avatars').remove();
        }
      });
    }.bind(this));

    // Close the tooltips
    DemoAvatars.AvatarsTooltipLike && DemoAvatars.AvatarsTooltipLike.close();
    DemoAvatars.AvatarsTooltipDislike && DemoAvatars.AvatarsTooltipDislike.close();
  });

  // If it's the inital jBox add onCloseComplete events
  initial && (jBoxAvatar.options.onCloseComplete = function () {
    // Loop through all modal jBoxes and remove them from DOM
    $.each(DemoAvatars.Modals, function (index, jBox) {
      jBox.destroy();
      delete DemoAvatars.Modals[jBox.id];
    });

    // Remove the tooltips from DOM
    DemoAvatars.AvatarsTooltipLike && DemoAvatars.AvatarsTooltipLike.destroy();
    DemoAvatars.AvatarsTooltipDislike && DemoAvatars.AvatarsTooltipDislike.destroy();
  });

  // Store the jBox in the modal collection
  DemoAvatars.Modals[jBoxAvatar.id] = jBoxAvatar;
}