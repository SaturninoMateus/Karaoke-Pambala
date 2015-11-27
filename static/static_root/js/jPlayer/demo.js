/*$(document).ready(function(){*/
$("#song2").click(function(){

  var myPlaylist = new jPlayerPlaylist({
    jPlayer: "#jplayer_N",
    cssSelectorAncestor: "#jp_container_N"
  }, [
    {
      title:"Busted Chump",
      artist:"ADG3",
      mp3:"/media/musicas/nobody_knows_you_pro.mp3",
      poster: "/static/images/m0.jpg"
    },/*{
      title:"Busted Chump",
      artist:"ADG3",
      mp3:"http://www.faroe.com/sites/default/files/adg3com_bustedchump.mp3",
      poster: "/static/images/m0.jpg"
    },*/
    {
      title:"Chucked Knuckles",
      artist:"3studios",
      mp3:"http://flatfull.com/themes/assets/musics/adg3com_chuckedknuckles.mp3",
      poster: "images/m0.jpg"
    },
    {
      title:"Cloudless Days",
      artist:"ADG3 Studios",
      mp3:"http://flatfull.com/themes/assets/musics/adg3com_cloudlessdays.mp3",
      poster: "images/m0.jpg"
    },
    {
      title:"Core Issues",
      artist:"Studios",
      mp3:"http://flatfull.com/themes/assets/musics/adg3com_coreissues.mp3",
      poster: "images/m0.jpg"
    },
    {
      title:"Cryptic Psyche",
      artist:"ADG3",
      mp3:"http://flatfull.com/themes/assets/musics/adg3com_crypticpsyche.mp3",
      poster: "images/m0.jpg"
    },
    {
      title:"Electro Freak",
      artist:"Studios",
      mp3:"http://flatfull.com/themes/assets/musics/adg3com_electrofreak.mp3",
      poster: "images/m0.jpg"
    },
    {
      title:"Freeform",
      artist:"ADG",
      mp3:"http://flatfull.com/themes/assets/musics/adg3com_freeform.mp3",
      poster: "images/m0.jpg"
    }
  ], {
    playlistOptions: {
      enableRemoveControls: true,
      autoPlay: true
    },
    swfPath: "js/jPlayer",
    supplied: "webmv, ogv, m4v, oga, mp3",
    smoothPlayBar: true,
    keyEnabled: true,
    audioFullScreen: false
  });
    //############################################T
    //#@TheOneID
/*    $(document).ready(function() {
	  	var player = new CDGPlayer(document.getElementById('karaoke-display'));
	  	player.load("/media/musicas/nobody_knows_you_pro.cdg");

		document.getElementById('song').addEventListener("playing", function() {
			player.play();

		});


	});*/
    $(document).on($.jPlayer.event.play, myPlaylist.cssSelector.jPlayer,  function(){
        //$('.musicbar').addClass('animate');
        var player = new CDGPlayer(document.getElementById('karaoke-display'));

        player.load("/media/musicas/nobody_knows_you_pro.cdg");
		player.play();
    });


    //############################################




  $(document).on($.jPlayer.event.pause, myPlaylist.cssSelector.jPlayer,  function(){
    $('.musicbar').removeClass('animate');
    $('.jp-play-me').removeClass('active');
    $('.jp-play-me').parent('li').removeClass('active');
  });

  $(document).on($.jPlayer.event.play, myPlaylist.cssSelector.jPlayer,  function(){
    $('.musicbar').addClass('animate');
  });

  $(document).on('click', '.jp-play-me', function(e){
    e && e.preventDefault();
    var $this = $(e.target);
    if (!$this.is('a')) $this = $this.closest('a');

    $('.jp-play-me').not($this).removeClass('active');
    $('.jp-play-me').parent('li').not($this.parent('li')).removeClass('active');

    $this.toggleClass('active');
    $this.parent('li').toggleClass('active');
    if( !$this.hasClass('active') ){
      myPlaylist.pause();
    }else{
      var i = Math.floor(Math.random() * (1 + 7 - 1));
      myPlaylist.play(i);
    }
    
  });
    myPlaylist.play();


  // video

  $("#jplayer_1").jPlayer({
    click: function () {
/*    ready: function () {*/
      $(this).jPlayer("setMedia", {
        title: "Big Buck Bunny",
        m4v: "http://flatfull.com/themes/assets/video/big_buck_bunny_trailer.m4v",
        ogv: "http://flatfull.com/themes/assets/video/big_buck_bunny_trailer.ogv",
        webmv: "http://flatfull.com/themes/assets/video/big_buck_bunny_trailer.webm",
        poster: "images/m41.jpg"
      });
    },
    swfPath: "js",
    supplied: "webmv, ogv, m4v",
    size: {
      width: "100%",
      height: "auto",
      cssClass: "jp-video-360p"
    },
    globalVolume: true,
    smoothPlayBar: true,
    keyEnabled: true
  });

});