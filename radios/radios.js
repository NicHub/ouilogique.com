"use strict";

/**
 * Load scripts asynchronously.
 * TODO: The playlist can be specified in the “playlist” GET parameter.
 * For example:
 * videowall.html?playlist=./assets/playlist_selection_1.js
 */
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const loadScript = (fileURL, async = true, type = "text/javascript") => {
    return new Promise((resolve, reject) => {
        try {
            const scriptElement = document.createElement("script");
            scriptElement.type = type;
            scriptElement.async = async;
            scriptElement.src = fileURL;

            scriptElement.addEventListener("load", (ev) => {
                resolve({ status: true });
            });

            scriptElement.addEventListener("error", (ev) => {
                reject({
                    status: false,
                    message: `Failed to load the script ＄{fileURL}`,
                });
            });

            document.body.appendChild(scriptElement);
        } catch (error) {
            reject(error);
        }
    });
};

["./radio_station_playlist.js"].forEach((elem) =>
    loadScript(elem)
        .then((data) => {
            main();
        })
        .catch((err) => {
            console.error(err);
        })
);

function main() {
    // Get all geo names and return an array containing only unique values.
    let geo_names = [];
    for (let _i = 0; _i < radio_station_playlist.length; _i++) {
        let geo_name = radio_station_playlist[_i]["geo_name"];
        geo_names.push(geo_name);
    }
    geo_names = geo_names.filter(
        (value, index, array) => array.indexOf(value) === index
    );

    // Loop through all geo names and create each station audio control.
    let html_code = "";
    for (let _i = 0; _i < geo_names.length; _i++) {
        html_code += `\n<h2>${geo_names[_i]}</h2>`;
        for (let _j = 0; _j < radio_station_playlist.length; _j++) {
            if (radio_station_playlist[_j]["geo_name"] !== geo_names[_i]) {
                continue;
            }
            const title =
                radio_station_playlist[_j]["live_urls"].length > 0
                    ? `<a href="${radio_station_playlist[_j]["live_urls"][0]}">${radio_station_playlist[_j]["station_name"]}</a>`
                    : `${radio_station_playlist[_j]["station_name"]}`;

            let stream_urls_string = "";
            for (
                let _k = 0;
                _k < radio_station_playlist[_j]["stream_urls"].length;
                _k++
            ) {
                stream_urls_string += `\n<source src="${radio_station_playlist[_j]["stream_urls"][_k]}">`;
            }

            html_code += `
                    <figure>
                        <figcaption>${title}</figcaption>
                        <audio
                            controls
                            onpause="decorate_active_audio(this);"
                            onplay="pause_other(this); decorate_active_audio(this); change_title('${radio_station_playlist[_j]["station_name"]}')"
                        >${stream_urls_string}</audio>
                    </figure>`;
        }
    }
    document.getElementById("target").innerHTML = html_code;
    console.log(html_code);
}

function pause_other(_e) {
    const audio_elems = document.querySelectorAll("audio");
    for (let _i = 0; _i < audio_elems.length; _i++) {
        if (audio_elems[_i] != _e) {
            audio_elems[_i].pause();
        }
    }
}

function decorate_active_audio(_e) {
    const audio_elems = document.querySelectorAll("audio");
    for (let _i = 0; _i < audio_elems.length; _i++) {
        if (audio_elems[_i].paused) {
            audio_elems[_i].classList.remove("playing");
        } else {
            audio_elems[_i].classList.add("playing");
        }
    }
}

function change_title(title) {
    document.title = `${title}`;
}
