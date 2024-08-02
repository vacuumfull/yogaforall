document.addEventListener('DOMContentLoaded', () => {

    let introDuration = 400,
        logoDuration = 700

    KUTE.to('#intro-animation .girlleftbottom.one', { opacity: 1 }, { duration: introDuration }).start()
    KUTE.to('#intro-animation .girlleftbottom.two', { opacity: 1 }, { duration: introDuration }).start()
    KUTE.to('#intro-animation .girlleft.one', { opacity: 1 }, { duration: introDuration, delay: introDuration }).start()
    KUTE.to('#intro-animation .girlleft.two', { opacity: 1 }, { duration: introDuration, delay: introDuration }).start()

    KUTE.to('#intro-animation .girlcenter.one', { opacity: 1 }, { duration: introDuration, delay: introDuration * 2 }).start()
    KUTE.to('#intro-animation .girlcenter.two', { opacity: 1 }, { duration: introDuration, delay: introDuration * 2 }).start()
    KUTE.to('#intro-animation .girlcenter.three', { opacity: 1 }, { duration: introDuration, delay: introDuration * 2 }).start()
    KUTE.to('#intro-animation .girlcenteroverlay.zero', { opacity: 1 }, { duration: introDuration, delay: introDuration * 2 }).start()

    KUTE.to('#intro-animation .girlright.one', { opacity: 1 }, { duration: introDuration, delay: introDuration * 3 }).start()
    KUTE.to('#intro-animation .girlright.two', { opacity: 1 }, { duration: introDuration, delay: introDuration * 3 }).start()

    KUTE.to('#intro-animation .girlrightbottom.one', { opacity: 1 }, { duration: introDuration, delay: introDuration * 4 }).start()
    KUTE.to('#intro-animation .girlrightbottom.two', { opacity: 1 }, { duration: introDuration, delay: introDuration * 4 }).start()
    KUTE.to('#intro-animation .girlrightbottom.three', { opacity: 1 }, { duration: introDuration, delay: introDuration * 4 }).start()

    setTimeout(() => {

        let logoTextAnimation = KUTE.to('.more_text', {text: window.introHeadText}, {delay: 500, duration: 3500});

        let twelve = KUTE.fromTo('.girlrightbottom.three', {path: '.girlrightbottom.three', translateX: 0, translateY: 0, }, { path: '.logoletters.twelve', translateX: -30, translateY: -370,  }, {
            duration: logoDuration, 
            easing: 'easingCubicInOut',
            delay: logoDuration * 4,
            onComplete: function() {
                document.getElementById('intro-animation').classList.add('__activted')
            }
        }).chain(logoTextAnimation).start()

        let eleven = KUTE.fromTo('.girlrightbottom.two', {path: '.girlright.two', translateX: 0, translateY: 0, }, { path: '.logoletters.eleven', translateX: -30, translateY: -370,  }, {
            duration: logoDuration, 
            easing: 'easingCubicInOut',
            delay: logoDuration * 4,
            onComplete: function() {
            }
        }).start()

        let ten = KUTE.fromTo('.girlrightbottom.one', {path: '.girlright.one',  translateX: 0, translateY: 0  }, { path: '.logoletters.ten', translateX: -30,  translateY: -370 }, {
            duration: logoDuration, 
            easing: 'easingCubicInOut',
            delay: logoDuration * 4,
            onComplete: function() {
            }
        }).start()

        let nine = KUTE.fromTo('.girlright.two', {path: '.girlright.two', translateX: 0, translateY: 0, }, { path: '.logoletters.nine', translateX: -30, translateY: -370,  }, {
            duration: logoDuration, 
            easing: 'easingCubicInOut',
            delay: logoDuration * 3,
            onComplete: function() {
            }
        }).start()

        let eight = KUTE.fromTo('.girlright.one', {path: '.girlright.one',  translateX: 0, translateY: 0  }, { path: '.logoletters.eight', translateX: -30,  translateY: -370 }, {
            duration: logoDuration, 
            easing: 'easingCubicInOut',
            delay: logoDuration * 3,
            onComplete: function() {
            }
        }).start()

        let seven =  KUTE.fromTo('.girlcenter.two', {path: '.girlleft.two', translateX: 0, translateY: 0, }, { path: '.logoletters.seven', translateX: -30, translateY: -370,  }, {
            duration: logoDuration, 
            delay: logoDuration * 2,
            easing: 'easingCubicInOut',
            onComplete: function() {
            }
        }).start()

        let six = KUTE.fromTo('.girlcenter.one', {path: '.girlcenter.one',  translateX: 0, translateY: 0  }, { path: '.logoletters.six', translateX: -30,  translateY: -370 }, {
            duration: logoDuration, 
            delay: logoDuration * 2,
            easing: 'easingCubicInOut',
            onComplete: function() {
                document.querySelector('.girlcenteroverlay.zero').style.visibility = 'hidden'
            }
        }).start()

        KUTE.fromTo('.girlcenteroverlay.zero', {path: '.girlcenteroverlay.zero',  translateX: 0, translateY: 0  }, { path: '.logoletters.five', translateX: -30,  translateY: -370 }, {
            duration: logoDuration, 
            delay: logoDuration * 2,
            easing: 'easingCubicInOut',
        }).start()

        let five = KUTE.fromTo('.girlcenter.three', {path: '.girlcenter.three',  translateX: 0, translateY: 0  }, { path: '.logoletters.five', translateX: -30,  translateY: -370 }, {
            duration: logoDuration, 
            delay: logoDuration * 2,
            easing: 'easingCubicInOut',

        }).start()

        let four = KUTE.fromTo('.girlleft.two', {path: '.girlleft.two', translateX: 0, translateY: 0  }, { path: '.logoletters.four', translateX: -30,  translateY: -370 }, {
            duration: logoDuration, 
            delay: logoDuration * 1,
            easing: 'easingCubicInOut',
            onComplete: function() {
            }
        }).start()

        let three =  KUTE.fromTo('.girlleft.one', {path: '.girlleft.one', translateX: 0, translateY: 0 }, { path: '.logoletters.three', translateX: -30, translateY: -370, }, {
            duration: logoDuration, 
            delay: logoDuration * 1,
            easing: 'easingCubicInOut',
            onComplete: function() {
            }
        }).start()

        let two = KUTE.fromTo('.girlleftbottom.two', {path: '.girlleftbottom.two', translateX: 0, translateY: 0 }, { path: '.logoletters.two', translateX: -30, translateY: -370, }, {
            duration: logoDuration, 
            easing: 'easingCubicInOut',
            onComplete: function() {
            }
        }).start()


        let one = KUTE.fromTo('.girlleftbottom.one',
            { path: '.girlleftbottom.one', translateX: 0, translateY: 0, attrs: {fill: '#fff'}}, 
            { path: '.logoletters.one', translateX: -30, translateY: -370,  attrs: {fill: '#000'} }, {
            duration: logoDuration, 
            easing: 'easingCubicInOut',
            onComplete: function() {
            }
        }).start()

        

    }, 2000)

})