/*****************************************************************************/
/*
CS10 -- staff.js
This file builds the staff images section from JSON data and makes working with
these images much easier. For each person:

Manually create/nickname object. (example, with all properties):
DanGarcia = {
    name: 'Sr. Lecturer SOE Dan Garcia',
    img: 'http://www.cs.berkeley.edu/~ddgarcia/gifs/DanGarciaUCBFaculty2004.jpg',
    imgSrc: 'DanGarcia.jpg',
    web: 'http://www.cs.berkeley.edu/%7Eddgarcia/',
    bio: 'DanBio.txt',
    email: 'ddgarcia@cs.berkeley.edu',
    info: '777 Soda, (510) 517-4041'
}
OR autogenerate simple object by adding string 'First Last' (here, 'Brandon Chen'):
BrandonChen = { name: 'Brandon Chen',
    img: 'Sp14/BrandonChen.jpg',
    imgSrc: 'BrandonChen.jpg' }
NOTE: All images must be in the proper folders and match the name, w/o spaces.
'imgSrc' should be a small image in the directory ~/public_html/images/small/ *
'img' should be a large image in the directory ~/public_html/images/(semester/yr, e.g. Sp14)/ *
If no image, add to LIST_OF_SHAME -- will display Alonzo instead.

There are a few lists of objects: instructors, tas, readers, las -- more can be created if necessary:
To add a new section:
1. Add a div with an ID to staff.html
2. Add the same ID name to the 'all' object.
3. Add a call to buildGroup(), with the ID name (string) and the number of
images per row (int)

edits: num images per row disabled

*/
/*****************************************************************************/

// JSON mappings for staff images / info.

DanGarcia = {
    name: 'Sr. Lecturer SOE Dan Garcia',
    img: 'DanGarciaUCBFaculty2004.jpg',
    imgSrc: 'DanGarcia.jpg',
    web: 'http://www.cs.berkeley.edu/%7Eddgarcia/',
    bio: 'http://inst.eecs.berkeley.edu/~cs10/sp14/bios/DanBio.txt',
    email: 'ddgarcia@cs.berkeley.edu',
    info: '777 Soda, (510) 517-4041' }

MichaelBall = {
    name: 'Michael Ball',
    img: 'Sp14/MichaelBallTake3.jpg',
    imgSrc: 'MichaelBall.jpg',
    web: 'http://michaelballphoto.com',
    bio: 'http://inst.eecs.berkeley.edu/~cs10/sp14/bios/MichaelBall.txt',
    email: 'cs10-ta@imail.eecs.berkeley.edu' }

maxD = {
    name: 'Max Dougherty',
    img: 'Sp14/MaxDougherty.jpg',
    imgSrc: 'MaxDougherty.jpg',
    email: 'mdougherty@berkeley.edu' }

IanBirnam = {
    name: 'Ian Birnam',
    img: 'Sp14/IanBirnam.jpg',
    imgSrc: 'IanBirnam.jpg',
    web: 'http://ianbirnam.com',
    bio: 'http://inst.eecs.berkeley.edu/~cs10/sp14/bios/IanBio.txt',
    email: 'ibirnam@berkeley.edu' }

jeffreyS = {
    name: 'Jeffrey Snowiss',
    img: 'Fa12/JeffreySnowiss.jpg',
    imgSrc: 'JeffreySnowiss.jpg',
    email: 'jasnowiss10@gmail.com' }

PeterSujan = {
    name: 'Peter Sujan',
    img: 'Fa12/PeterSujan.jpg',
    imgSrc: 'PeterSujan.jpg',
    bio: 'http://inst.eecs.berkeley.edu/~cs10/sp14/bios/PeterBio.txt',
    email: 'peterasujan@berkeley.edu' }

victoriaS = {
    name: 'Victoria Shi',
    img: 'Fa13/VictoriaShi.jpg',
    imgSrc: 'VictoriaShi.jpg',
    email: 'victoria.shi@berkeley.edu' }

rachelH = {
    name: 'Rachel Huang',
    img: 'Fa13/RachelHuang.jpg',
    imgSrc: 'RachelHuang.jpg',
    email: 'rachelhuang072@berkeley.edu' }

jannaG = {
    name: 'Janna Golden',
    img: 'Sp14/JannaGolden.jpg',
    imgSrc: 'JannaGolden.jpg',
    email: 'jannagolden@berkeley.edu' }
sumerM = {
    name: 'Sumer Mohammed',
    img: 'Fa12/SumerMohammed.jpg',
    imgSrc: 'SumerMohammed.jpg',
    email: 'sumermohammed@berkeley.edu' }

josephC = {
    name: 'Joseph Cawthorne',
    img: 'Fa13/JosephCawthorne.jpg',
    imgSrc: 'JosephCawthorne.jpg' }
    
songS   = {
    name: 'Song Sok',
    img: 'Fa13/SongSok.jpg',
    imgSrc: 'SongSok.jpg' }
    
claireW = {
    name: 'Claire Watanabe',
    img: 'Fa13/ClaireWatanabe.jpg',
    imgSrc: 'ClaireWatanabe.jpg' }
    
jaclynB = {
    name: 'Jaclyn Burge',
    img: 'Fa13/JaclynBurge.jpg',
    imgSrc: 'JaclynBurge.jpg' }
    
andyS   = {
    name: 'Andrew Schmitt',
    img: 'Sp14/AndrewSchmitt.jpg',
    imgSrc: 'AndrewSchmitt.jpg' }

LaurenMock = {
    name: 'Lauren Mock',
    img: 'Sp14/LaurenMock.jpg',
    imgSrc: 'LaurenMock.jpg',
    web: 'http://linkedin.com/in/laurenmock',
    email: 'lmock@berkeley.edu' }

KunalMarwaha = { name: 'Kunal Marwaha',
    img: 'Sp14/KunalMarwaha.jpg',
    imgSrc: 'KunalMarwaha.jpg',
    email: 'marwahaha@berkeley.edu'}

KyleZentner = { name: 'Kyle Zentner',
    img: 'Sp14/KyleZentner.jpg',
    imgSrc: 'KyleZentner.jpg' }

JocelynTakahashi = { name: 'Jocelyn Takahashi',
    img: 'Sp13/JocelynTakahashi.jpg',
    imgSrc: '../Sp13/t/JocelynTakahashi.jpg' }
    
benC = { name: 'Ben Carvalho',
    img: 'Fa13/BenCarvalho.jpg',
    imgSrc: 'BenCarvalho.jpg',
    bio: 'http://inst.eecs.berkeley.edu/~cs10/sp14/bios/BenjaminCarvalhoBio.txt' }
    
oliverO = { name: 'Oliver O\'Donnell',
    img: 'Sp14/OliverODonnell.jpg',
    imgSrc: 'OliverODonnell.jpg',
    bio: 'http://inst.eecs.berkeley.edu/~cs10/sp14/bios/Oliver ODonnell.txt' }
    
carenT = { name: 'Caren Thomas',
    img: 'Sp14/CarenThomas.jpg',
    imgSrc: 'CarenThomas.jpg',
    bio: 'http://inst.eecs.berkeley.edu/~cs10/sp14/bios/CarenThomasBio.txt' }

paulI = { name: 'Paul Irwin',
    img: 'Fa13/PaulIrwin.jpg',
    imgSrc: 'PaulIrwin.jpg' }

jessicaA = { name: 'Jessica Andrich',
    img: 'Fa13/JessicaAndrich.jpg',
    imgSrc: 'JessicaAndrich.jpg' }
    
pierce = { name: 'Pierce Vollucci',
    img: 'Fa13/PierceVollucci.jpg',
    imgSrc: 'PierceVollucci.jpg' }
    
mridula = {name: 'Mridula Dilip',
    img: 'Sp14/MrindulaDilip.jpg',
    imgSrc: 'MrindulaDilip.jpg' }
/*****************************************************************************/
/** LIST DEFINITIONS **/
/*****************************************************************************/

instructors = [ pierce ];

tas = [rachelH, benC, KunalMarwaha]

readers = [ 'Veersuvrat Rajpal', 'Adam Kuphaldt' ]

labdev = [ PeterSujan, LaurenMock, jessicaA, paulI, andyS, 'Liuxiao Zhang',
           'Manisha Sharma', 'Samy Hajal', 'Sulaiman Haruna' ]

edx = [ KunalMarwaha,
        'Sean Scofield',
        'Akhila Raju',
        'Josh Perline',
        'Manisha Sharma',
        mridula,
        'Nick Rose',
        'Nidhi Swamy',
        'Sneha Dilip',
        'Yuan Yuan'  ]

snap = [ KunalMarwaha,
         'Brandon Chen',
         'Dibyo Majundar',
         'Janet Chu',
         'Jesar Shah',
         'Joey Barreto',
         'Irene Lee',
         'Kyle Hotchkiss',
         KyleZentner,
          'Michelle Han',
         'Natasha Sandy',
         'Sara Seacat',
          'Sean Scofield',
         'Yuan Yuan',
         ]


// If you need to add a new SECTION add it to this object.
// Follow the same format.
all = {
    instructors: instructors,
    las: las,
    readers: readers,
    tas: tas,
    edx: edx,
    snap: snap,
    labdev: labdev,
};

LIST_OF_SHAME = [
'VirajMahesh.jpg',
'AngelaSo.jpg',
'HarshMujoo.jpg',
'HunterBrown.jpg',
'IreneLee.jpg',
'JesarShah.jpg',
'JiJunChen.jpg',
'JisooHan.jpg',
'MichelleHan.jpg',
'NavsharanSingh.jpg',
'NicholasDill.jpg',
'PriscillaBermudez.jpg',
'RebeccaKuan.jpg',
'SamyHajal.jpg',
'SerenaChan.jpg',
'StephenShan.jpg',
'StevenHolman.jpg',
'VictorSolis.jpg' ]


/*****************************************************************************/
/* DATA POPULATION FUNCTIONS  */
/*****************************************************************************/

// Build a basic object for a person from the current semester.
function baseObj(name) {
    src = name.replace(/ /g , '')
    return { name: name,
             img: 'Sp14/' + src + '.jpg',
             imgSrc: src + '.jpg' }
}

function buildPerson(data, width) {
    // Given a JSON object build a div that contains all the person's info
    // width is used to control how many are on a row on the page.

    // Build data objects for very simple cases with nothing special.
    if (data.constructor === String) {
        data = baseObj(data)
    }

    // If there's no image, use 3D Alonzo
    if (!data.imgSrc || LIST_OF_SHAME.indexOf(data.imgSrc) !== -1) {
        data.imgSrc = '../NPY3D.jpg'
        data.img    = ''
    }
    // Create a table element with this person's data, setting a class for width
    elm = '<div style="display:table-cell">'
    if (!!data.img) {
        elm += '<a href=\'https://inst.eecs.berkeley.edu/~cs10/sp14/images/' + data.img + '\'>'
    }
    elm += '<img class=\'staff\' width=\'200\' height=\'300\' align=\'center\' '
    elm += 'alt=\'' + data.name + '\' title=\'' + data.name + '\' src=\'https://inst.eecs.berkeley.edu/~cs10/images/small/'
    elm += data.imgSrc + '\' />'
    if (!!data.img) {
        elm += '</a>'
    }
    elm += '<br /><strong>'
    if (!!data.web) {
        elm += '<a href=\'' + data.web + '\'>' + data.name + '</a>'
    } else {
        elm += data.name
    }
    elm += '</strong> '
    if (!!data.bio) {
        elm += '(<a href=\'' + data.bio + '\'>bio</a>)'
    }
    if (!!data.email) {
        elm += '<br /><a style=\'font-size:10px\' href=\'mailto:' + data.email +
        '?subject=[CS10] SUBJECT\'><code style=\'font-size:10px\'>' + data.email + '</code></a>';
    }
    if (!!data.info) {
        elm +=  '<br />' + data.info
    }
    elm += '</div>';
    return elm;
}

function buildGroup(group, w) {
    // Build a set of table rows, with W items per row
    // based on the people in the GROUP
    // Add them to the appropriate HTML table element
    ppl = all[group]
    doc = document.getElementById(group)
    content = ''
    for (var i = 0; i < ppl.length; i += w) {
        content += '<div style=\'margin-bottom:20px\' class=\'staffimg\'>'
        for(var j = i; j < (i + w) && j < ppl.length; j += 1) {
            if (i + w > ppl.length) {
                 w = ppl.length - i
             }
            content += buildPerson(ppl[j], w)
        }
        content += '</div>'
        // content += '<div style=\'clear: both;\'></div>';
    }
    doc.innerHTML += content
}

function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      if (oldonload) {
        oldonload();
      }
      func();
    }
  }
}

addLoadEvent(function() {
  /* more code to run on page load */
  // Parameters: a section (HTML 'id') and num of images per row.
  buildGroup('instructors', 1)
  buildGroup('tas', 5)
  buildGroup('readers', 5)
  buildGroup('las', 5)
  buildGroup('edx', 5)
  buildGroup('labdev', 5)
  buildGroup('snap', 5)
})