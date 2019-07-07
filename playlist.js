const fs = require('fs');
const ytlist = require('youtube-playlist');
const ytdl = require('ytdl-core');

const urls =
[
    
    'https://www.youtube.com/playlist?list=UU-2Y8dQb0S6DtpxNgAKoJKA', //playstation
    'https://www.youtube.com/playlist?list=UUUnRn1f78foyP26XGkRfWsA', //gamespot trailers
    'https://www.youtube.com/playlist?list=UU0NwzCHb8Fg89eTB5eYX17Q', // skin spotlights
    'https://www.youtube.com/playlist?list=UU_ntXHv-XdKCD7CPynVvnQw', // bandai namco
    'https://www.youtube.com/playlist?list=UUjBp_7RuDBUYbd1LegWEJ8g', // xbox
   
];

urls.map(vidDownload);

function vidDownload(url) {
    let vidName,vidUrl;
   

    ytlist(url, ['name', 'url']).then(res =>{
        vidName = res.data.playlist[0].name;
        vidUrl = res.data.playlist[0].url;
        vidName = vidName.replace(/\W/g, '');

        ytdl(vidUrl)
        .pipe(fs.createWriteStream("temp/" + vidName + ".mp4")
        .on('error', function(err){
            console.log(err);
        }));
        
    })
}
