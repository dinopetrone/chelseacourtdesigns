var CCD = {
	
	/**
	* Run pre dom-ready initialization code
	* 
	*/
	init: function(){
		
		// Save context
		var self = this;
		
		// Will supress console.log() if false or removed. Only for use in dev, remove for production.
        self.debug = true;

		// Set CCD.support.ie
        self.support.testie();		

		// Call functions when DOM is ready, with proper context
        $(document).ready(self.domReady.call(self));

	},
	
	// Common lookups
	cache: {
	
		body: $('body'),
		window: $(window),
		nav: $('#primary-nav')		
	},
	
	currentPage:undefined,
	firstVisit:true,
	
	support: {
				
		/**
        * Test for IE.
        * If browser is IE, returns version number. Otherwise returns undefined
        * Example Usage: if(Builium.support.ie)
        * Source: https: gist.github.com/527683
        *
        */
        testie: function () {
            var undef,
		        v = 3,
		        div = document.createElement('div'),
		        all = div.getElementsByTagName('i');

            do {
                div.innerHTML = '<!--[if gt IE ' + (++v) + ']><i></i><![endif]-->';
            } while (all[0]);

            this['ie'] = v > 4 ? v : undef;
        }

	
		
		
	},
	
	/** 
	* Namespace for variables needed on runtime
	*
	*/
	globals: {},
	
	/** 
	* Namespace for global functions
	*
	*/
	utils: {
		
		
		
	},
	
	/**
	* Modals
	*
	* @name modal
	*
	*/
	modal: {
		
		currentModal: undefined,
		imageModalMarkup: '<figure><img src="{{img_url}}" width="880" height="466" /></figure>',
		
		show: function(){
			
			if (!arguments.length) return;

	        var self = this,
				args = arguments[0],
				target;

	        // If there's only 1 argument, we're being passed a selector or HTML snippet.
	        if (typeof args === 'string') {

				target = $('#' + args);

				// Open modal using passed selector
				if (target.length) target.modal();

				// Opam modal using passed html
				else $.modal(args);
	
			// If argument 'imgUrl' is passed, we're only showing the image
			} else if (typeof args === 'object' && args.hasOwnProperty('imgUrl')) {
				
				$.modal( self.imageModalMarkup.replace( '{{img_url}}', args.imgUrl ) , {containerId: 'screenshot-modal'});

	        // Otherwise, we're being passed options to init the modal.
	        } else if (typeof args === 'object' && args.hasOwnProperty('target')) {

				$('#' + args.target).modal(args);
				
	        }
		},
		
		configure: function(){
			if(!$.hasOwnProperty('modal')) return false;
			
			// Set default Simple Modal options
			$.modal.defaults.closeClass = 'modalClose';
			$.modal.defaults.closeHTML = '<a href="" class="modalCloseImg">Close</a>';
			$.modal.defaults.opacity = 80;
			$.modal.defaults.persist = true;
			$.modal.defaults.overlayClose = true;
			// $.modal.defaults.overlayClose = true;
			$.modal.defaults.onOpen = function(dialog) {
				if( dialog.data.get(0).id === 'contact-form' ) {
					if(CCD.globals.contactOpen) {
						dialog.overlay.show();
						dialog.container.removeClass('persist-hidden');
						setTimeout(function(){
							dialog.wrap.addClass('scroll')
						}, 2000)
					} else {
						dialog.overlay.fadeIn();
						dialog.data.show();
						dialog.container.fadeIn();
						CCD.globals.contactOpen = true;
						
					}
					
				} else {
					dialog.overlay.fadeIn();
					dialog.data.show();
					dialog.container.fadeIn();
				}
			};
		}
		
	},
	
	pages: {
		home: function(){
			var self = this;
			var slideshow = $('#slideshow');
			slideshow.find('li').removeClass('noshow');

			window.interval = setInterval(function(){
				var el = slideshow.find('li').eq(3);
				if(CCD.detector.isiPad() || CCD.detector.isMobile()) {
					el.attr('style','-webkit-transition: opacity 1s linear;transition: opacity 1s linear;opacity:0');
					setTimeout(function(){
						el.prependTo(slideshow).removeAttr('style');
					},2000)
				} else {
					el.fadeOut(1000,function(){
						el.prependTo(slideshow).show();
					});
				}

			},5000);	
		},
		
		about: function(){
			var aboutTabs = $("#about-tabs"),
				whoContainer = $('#who-container'),
				whatContainer = $('#what-container'),
				whoTabs = $('#who-tabs'),
				sascha = $('#sascha'),
				marie = $('#marie'),
				hillary = $('#hillary'),
				activeWho = marie;

			$('#what-btn').bind('click',function(){

				aboutTabs.find('.active').removeClass('active');
				$(this).addClass('active');

				whoContainer.fadeOut(function(){
					whatContainer.fadeIn();
				});

				return false;
			});
			$('#who-btn').bind('click',function(){

				aboutTabs.find('.active').removeClass('active');
				$(this).addClass('active');

				whatContainer.fadeOut(function(){
					whoContainer.fadeIn();
				});

				return false;
			});

			whoTabs.delegate('a','click',function(){
				var target = $( $(this).attr('href') );

				whoTabs.find('.active').removeClass('active');
				$(this).addClass('active');

				activeWho.fadeOut(function(){
					target.fadeIn();
				});

				activeWho = target;

				return false;

			});
		},
		
		portfolio: function(){
			$('#portfolio').delegate('a','click',function(e){
				$.modal('<img src="' + $(this).attr("href") + '" />',{
					overlayClose:true,
					persist:false
				});
				e.preventDefault()
			});

			$('body').delegate('#simplemodal-container','click',function(){
				$.modal.close()
			});

			$('#portfolio').find('a').each(function(){
				(new Image()).src = $(this).attr('href');
			});
		}
	},
	
	
	domReady: function(){
		var self = this,
			timeout = null;
	
		if(self.detector.isiPad() || self.detector.isMobile()) {
			$('html').addClass('iOS');
		}
		
		// Initiate modal congifuration
        self.modal.configure();

		// Add iOS class to body if iOS
		if(self.detector.isiPad() || self.detector.isMobile()) {
			self.cache.body.addClass('iOS');
		}
		
		$('#main').delegate('.contact-action','click',function(e){
			e.preventDefault();
			CCD.modal.show({
				target:'contact-form',
				persist:true,
				onClose:function(dialog){
					
					$.modal.persistClose();
					// console.log(dialog);
				}
			});
		});

	},
	
	iOSHelper: function(){
		
	},
	
	/* 
	 * User detection is frowned upon, but can be useful. Use with caution and only when needed 
	 * 
	 * Detection is cached after first call to a given method.
	*/
	detector: {

	    getAgent: function() {
	        return navigator.userAgent.toLowerCase();
	    },

	    isWebKit: function(userAgent) {
	        if(this._isWebKit === undefined) {
	            var agent = userAgent || this.getAgent();
	            this._isWebKit =  !!agent.match(/AppleWebKit/i);
	            this.isWebKit = function() {
	                return this._isWebKit;
	            };
	        }
	        return this._isWebKit;
	    },

		// returns true if agent is iPad
	    isiPad: function(userAgent) {
	        var agent = userAgent || this.getAgent();
	        return !!(this.isWebKit(agent) && agent.match(/ipad/i));
	    },

		// returns true if agent is iPhone or iPod Touch
	    isMobile: function(userAgent) {
	        var agent = userAgent || this.getAgent();
	        return this.isWebKit(agent) && (agent.match(/Mobile/i) && !this.isiPad(agent));
	    },
	
		hasFlash: function() {
			if(this._hasFlash === undefined) {
				this._hasFlash = false;
				try {
				  var fo = new ActiveXObject('ShockwaveFlash.ShockwaveFlash');
				  if(fo) this._hasFlash = true;
				} catch(e) {
				  if(navigator.mimeTypes['application/x-shockwave-flash'] != undefined) this._hasFlash = true;
				}
				if(!this._hasFlash) CCD.cache.body.addClass('no-flash');
			}
			
			return this._hasFlash;
		}

	},
	
	/**
    * Rewrite the console functionality to not break IE or surpress console.log() if debugging is off
    * 
    * @name console
    * @author GN
    */
    console: function () {
        if (!window.console || !this.hasOwnProperty('debug')) {
            window.console = {};
            var f = function () { },
				methods = ['log', 'debug', 'info', 'warn', 'error', 'time', 'timeEnd', 'group', 'groupEnd'];
			for(var i = 0, length = methods.length; i<length; i++){
				window.console[item] = f;
			}	
        }
    }

	
	
}

CCD.init();