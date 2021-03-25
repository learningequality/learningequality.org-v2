import '@babel/polyfill';
/* feature:use_react */
import React from 'react';
import ReactDOM from 'react-dom';
import TestReact from './components/TestReact';
import MobileMenu from './components/mobile-menu';
import MobileSubMenu from './components/mobile-sub-menu';
import DesktopSubMenu from './components/desktop-sub-menu';
import DesktopCloseMenus from './components/desktop-close-menus';
import SkipLink from './components/skip-link';
import CookieWarning from './components/cookie-message';
import Accordion from './components/accordion';
import Carousel from './components/carousel';
import ProgressBar from './components/progress-bar';
import VideoModal from './components/video-modal';
import Tabs from './components/tabs';

// IE11 polyfills
import foreachPolyfill from './polyfills/foreach-polyfill';
import closestPolyfill from './polyfills/closest-polyfill';

import '../sass/main.scss';

foreachPolyfill();
closestPolyfill();

// Open the mobile menu callback
function openMobileMenu() {
    document.querySelector('body').classList.add('no-scroll');
    document.querySelector('[data-mobile-menu]').classList.add('is-visible');
}

// Close the mobile menu callback.
function closeMobileMenu() {
    document.querySelector('body').classList.remove('no-scroll');
    document.querySelector('[data-mobile-menu]').classList.remove('is-visible');
}

document.addEventListener('DOMContentLoaded', () => {
    /* eslint-disable no-restricted-syntax, no-new */

    const cookie = document.querySelector(CookieWarning.selector());
    new CookieWarning(cookie);
    for (const accordion of document.querySelectorAll(Accordion.selector())) {
        new Accordion(accordion);
    }
    for (const carousel of document.querySelectorAll(Carousel.selector())) {
        new Carousel(carousel);
    }

    for (const mobilemenu of document.querySelectorAll(MobileMenu.selector())) {
        new MobileMenu(mobilemenu, openMobileMenu, closeMobileMenu);
    }

    for (const mobilesubmenu of document.querySelectorAll(
        MobileSubMenu.selector(),
    )) {
        new MobileSubMenu(mobilesubmenu);
    }

    for (const desktopsubmenu of document.querySelectorAll(
        DesktopSubMenu.selector(),
    )) {
        new DesktopSubMenu(desktopsubmenu);
    }

    new DesktopCloseMenus();

    for (const progressbar of document.querySelectorAll(
        ProgressBar.selector(),
    )) {
        new ProgressBar(progressbar);
    }

    for (const videomodal of document.querySelectorAll(VideoModal.selector())) {
        new VideoModal(videomodal);
    }

    for (const tabs of document.querySelectorAll(Tabs.selector())) {
        new Tabs(tabs);
    }

    for (const skiplink of document.querySelectorAll(SkipLink.selector())) {
        new SkipLink(skiplink);
    } // Test react - add a div with a data attribute of `data-test-react` to test

    /* feature:use_react */
    // Test react - add a div with a data attribute of `data-test-react` to test
    for (const element of document.querySelectorAll('[data-test-react]')) {
        ReactDOM.render(<TestReact greeting="boo!" />, element);
    }
});
