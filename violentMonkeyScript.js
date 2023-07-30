// ==UserScript==
// @name         Clubhouse Room Downloader
// @namespace    clubhouse-room-downloader
// @version      1.0
// @description  Download the M3U file of clubhouse to extract the audio later
// @match        https://www.clubhouse.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Override the XMLHttpRequest object
    var originalXHR = window.XMLHttpRequest;

    function newXHR() {
        var realXHR = new originalXHR();

        realXHR.addEventListener('load', function() {
            var responseURL = realXHR.responseURL;
            if (responseURL.startsWith('https://www.clubhouse.com/web_api/get_replay_channel_playlist')) {
                var button = document.createElement('button');
                button.textContent = 'Download Audio';
                button.style.cssText = 'position: fixed; top: 10px; left: 10px; z-index: 99999999999; padding: 10px; font-size: 14px; font-weight: bold; color: #fff; background-color: #1E90FF; border: none; border-radius: 4px; cursor: pointer; text-decoration: none;';
                button.addEventListener('click', function() {
                    window.open(responseURL, '_blank');
                });
                document.body.appendChild(button);
            }
        });

        return realXHR;
    }

    // Replace the native XMLHttpRequest with the overridden version
    window.XMLHttpRequest = newXHR;
})();
