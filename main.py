# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.

VIDEOS = {'The Murdoch Diaries':
              [{'name': 'The Murdoch Diaries',
                'thumb': 'https://i.ytimg.com/vi/K8SgmZFrs7A/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBJeZX0FQlnlrvu6MfPBBb0zoP4Fw',
                'video': 'https://cheekyvideos.net/murdoch/videos/The%20Murdoch%20Diaries.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'Shills',
                'thumb': 'https://i.ytimg.com/vi/_Kw_ntPqdkw/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLB8xnUkgDXD4fbVoHMyEiVbX0HamQ',
                'video': 'https://cheekyvideos.net/murdoch/videos/Shills.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'Pure 100% Bavarian Phenotype',
                'thumb': 'https://i.ytimg.com/vi/_jZyYqbBmpY/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLC7SJyxzfJVDGXbQ3mU6A8iupw6Jw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Pure%20100%20Bavarian%20Phenotype.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'Revenge of the Murdochs',
                'thumb': 'https://i.ytimg.com/vi/0jKOaZNGxYA/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLAoZOSawXhLxcL3atyLBm3fLvwzGw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Revenge%20of%20the%20Murdochs.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'HuWhite Knights',
                'thumb': 'https://i.ytimg.com/vi/GlBrfKQ04yk/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBWnIbvet8BiWPTj7LX23RtKDWTag',
                'video': 'https://cheekyvideos.net/murdoch/videos/Hwite%20Knights.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'Meme Magic',
                'thumb': 'https://i.ytimg.com/vi/MGE8lNzq1as/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLCpy3-4HBapTWgteX3KRywgiQR11Q',
                'video': 'https://cheekyvideos.net/murdoch/videos/Meme%20Magic.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'The Great Meme War of 2016',
                'thumb': 'https://i.ytimg.com/vi/5OTiTnknyDw/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDqwW0MWUAxqUU5_jbt3UIG5zqbLQ',
                'video': 'https://cheekyvideos.net/murdoch/videos/The%20Great%20Meme%20War%20of%202016.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'The Alt Light Strikes Back',
                'thumb': 'https://i.ytimg.com/vi/08GR1_0Nflo/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLC3LDpLKiFTaeGmPjOtMSt7e1O3QA',
                'video': 'https://cheekyvideos.net/murdoch/videos/THE%20ALT%20LIGHT%20STRIKES%20BACK.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'Your Heroes Journey',
                'thumb': 'https://i.ytimg.com/vi/du1VW6n1Hvs/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLAfQMqevH8Ijpt0ugWLrtaHPAiIvA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Your%20Heroes%20Journey.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'The Last Stand of Implicit Whiteness',
                'thumb': 'https://i.ytimg.com/vi/czrv0-2b3i4/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLB4ben_PbEkt69oSHFei1Ix7vBRiw',
                'video': 'https://cheekyvideos.net/murdoch/videos/The%20Last%20Stand%20of%20Implicit%20Whiteness.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'TLSOIW AND TRRPB (HATE SPEECH EDIT)',
                'thumb': 'https://i.ytimg.com/vi/tCfbeF8BT6k/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDu_pGt4NGmd6z45Gddoc4a_qUEzA',
                'video': 'https://cheekyvideos.net/murdoch/videos/TLSOIW%20AND%20TRRPB%20%28HATE%20SPEECH%20EDIT%29.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'All For Love',
                'thumb': 'https://i.ytimg.com/vi/Xk0Tm1-DDSE/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDTsnKxrB7IBPfAB-KwyuAFMvWMMw',
                'video': 'https://cheekyvideos.net/murdoch/videos/All%20For%20Love.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'Nice Guy National Socialist',
                'thumb': 'https://i.ytimg.com/vi/ottANpOE2Nc/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBIRLL5GJWY-stX0w7kVy1_2r-oVA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Nice%20Guy%20National%20Socialist.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'Metamorphosis',
                'thumb': 'https://i.ytimg.com/vi/-4dKwOMlS78/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBmKMtP3ejswzFT63G5gQdOlKknNA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Metamorphosis.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'Get yer hands off muh vidya',
                'thumb': 'https://i.ytimg.com/vi/LMZjJh2BHGs/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLCM88MVyM4b9dH-hhJj4coXTkmIZg',
                'video': 'https://cheekyvideos.net/murdoch/videos/Get%20yer%20hands%20off%20muh%20vidya.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'The Cruel Fate of Kekistan',
                'thumb': 'https://i.ytimg.com/vi/pYS9fLucyt8/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLAD6X5e6hPGF-TuqA5Z4SMIfk_5-g',
                'video': 'https://cheekyvideos.net/murdoch/videos/The%20Cruel%20Fate%20of%20Kekistan.mp4',
                'genre': 'The Murdoch Diaries'},
               {'name': 'Speak Freely',
                'thumb': 'https://i.ytimg.com/vi/odw2lyLPd24/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBYEPIMHY5UHUdiyMZCpPTc3TYdUw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Speak%20Freely.mp4',
                'genre': 'The Murdoch Diaries'}
                ],
          'Classic':
              [{'name': 'Episode 1  The reddit cuck discovers pol',
                'thumb': 'https://i.ytimg.com/vi/K8SgmZFrs7A/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBJeZX0FQlnlrvu6MfPBBb0zoP4Fw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%201%20%20The%20reddit%20cuck%20discovers%20%20pol.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 2  Nigel\'s Dream',
                'thumb': 'https://i.ytimg.com/vi/_Kw_ntPqdkw/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLB8xnUkgDXD4fbVoHMyEiVbX0HamQ',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%202%20%20Nigel\'s%20Dream.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 3  The Orbiter',
                'thumb': 'https://i.ytimg.com/vi/_jZyYqbBmpY/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLC7SJyxzfJVDGXbQ3mU6A8iupw6Jw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%203%20%20The%20Orbiter.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 4  Return of the Swede',
                'thumb': 'https://i.ytimg.com/vi/0jKOaZNGxYA/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLAoZOSawXhLxcL3atyLBm3fLvwzGw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%204%20%20Return%20of%20the%20Swede.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 5 brave',
                'thumb': 'https://i.ytimg.com/vi/GlBrfKQ04yk/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBWnIbvet8BiWPTj7LX23RtKDWTag',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%205%20%20brave.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 6  Ellen Pao\'s gift to  pol',
                'thumb': 'https://i.ytimg.com/vi/MGE8lNzq1as/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLCpy3-4HBapTWgteX3KRywgiQR11Q',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%206%20%20Ellen%20Pao\'s%20gift%20to%20%20pol.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 7  The Ghost of Stonewall Jackson',
                'thumb': 'https://i.ytimg.com/vi/5OTiTnknyDw/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDqwW0MWUAxqUU5_jbt3UIG5zqbLQ',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%207%20%20The%20Ghost%20of%20Stonewall%20Jackson.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 8  Flight 800-000',
                'thumb': 'https://i.ytimg.com/vi/08GR1_0Nflo/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLC3LDpLKiFTaeGmPjOtMSt7e1O3QA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%208%20%20Flight%20800-000.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 9  J.J.\'s Interracial Art That\'s Perfectly Acceptable',
                'thumb': 'https://i.ytimg.com/vi/du1VW6n1Hvs/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLAfQMqevH8Ijpt0ugWLrtaHPAiIvA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%209%20%20J.Js%20Interracial%20Art%20That\'s%20Perfectly%20Acceptable%20To%20Be%20Put%20On%20YouTube.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 10  When My Brothers Finally Wake Up',
                'thumb': 'https://i.ytimg.com/vi/czrv0-2b3i4/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLB4ben_PbEkt69oSHFei1Ix7vBRiw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%2010%20%20When%20My%20Brothers%20Finally%20Wake%20Up.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 11  Mandell\'s milk',
                'thumb': 'https://i.ytimg.com/vi/tCfbeF8BT6k/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDu_pGt4NGmd6z45Gddoc4a_qUEzA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%2011%20%20Mandell\'s%20milk.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 12  The Art of the Red Pill',
                'thumb': 'https://i.ytimg.com/vi/Xk0Tm1-DDSE/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDTsnKxrB7IBPfAB-KwyuAFMvWMMw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%2012%20%20The%20Art%20of%20the%20Red%20Pill.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 13  Prep The Bull',
                'thumb': 'https://i.ytimg.com/vi/ottANpOE2Nc/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBIRLL5GJWY-stX0w7kVy1_2r-oVA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%2013%20%20Prep%20The%20Bull.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 14  Progressives Night Out',
                'thumb': 'https://i.ytimg.com/vi/-4dKwOMlS78/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBmKMtP3ejswzFT63G5gQdOlKknNA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%2014%20%20Progressives%20Night%20Out.mp4',
                'genre': 'Classic'},
               {'name': 'Episode 15  Hold Back The Night',
                'thumb': 'https://i.ytimg.com/vi/LMZjJh2BHGs/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLCM88MVyM4b9dH-hhJj4coXTkmIZg',
                'video': 'https://cheekyvideos.net/murdoch/videos/Episode%2015%20Hold%20Back%20The%20Night.mp4',
                'genre': 'Classic'}
               ],
          'Misc':
              [{'name': 'Race War Us Against Them',
                'thumb': 'https://i.ytimg.com/vi/K8SgmZFrs7A/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBJeZX0FQlnlrvu6MfPBBb0zoP4Fw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Race%20War,%20Us%20Against%20Them.mp4',
                'genre': 'Misc'},
               {'name': 'Murdoch Halloween Special 1',
                'thumb': 'https://i.ytimg.com/vi/_Kw_ntPqdkw/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLB8xnUkgDXD4fbVoHMyEiVbX0HamQ',
                'video': 'https://cheekyvideos.net/murdoch/videos/Murdoch%20Halloween%20Special%201.mp4',
                'genre': 'Misc'},
               {'name': 'The Last Son of the West',
                'thumb': 'https://i.ytimg.com/vi/_jZyYqbBmpY/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLC7SJyxzfJVDGXbQ3mU6A8iupw6Jw',
                'video': 'https://cheekyvideos.net/murdoch/videos/The%20Last%20Son%20of%20the%20West.mp4',
                'genre': 'Misc'},
               {'name': 'Murdoch\'s Christmas Special 1',
                'thumb': 'https://i.ytimg.com/vi/0jKOaZNGxYA/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLAoZOSawXhLxcL3atyLBm3fLvwzGw',
                'video': 'https://cheekyvideos.net/murdoch/videos/Murdoch\'s%20Christmas%20Special%201.mp4',
                'genre': 'Misc'},
               {'name': 'This Machine Kills Hippies',
                'thumb': 'https://i.ytimg.com/vi/GlBrfKQ04yk/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBWnIbvet8BiWPTj7LX23RtKDWTag',
                'video': 'https://cheekyvideos.net/murdoch/videos/This%20Machine%20Kills%20Hippies.mp4',
                'genre': 'Misc'},
               {'name': 'Jeb ON SUICIDE WATCH',
                'thumb': 'https://i.ytimg.com/vi/MGE8lNzq1as/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLCpy3-4HBapTWgteX3KRywgiQR11Q',
                'video': 'https://cheekyvideos.net/murdoch/videos/Jeb%20ON%20SUICIDE%20WATCH.mp4',
                'genre': 'Misc'},
               {'name': 'Back to the Faggot',
                'thumb': 'https://i.ytimg.com/vi/5OTiTnknyDw/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDqwW0MWUAxqUU5_jbt3UIG5zqbLQ',
                'video': 'https://cheekyvideos.net/murdoch/videos/Back%20to%20the%20Faggot.mp4',
                'genre': 'Misc'},
               {'name': 'Trudeau\'s Diversityathon',
                'thumb': 'https://i.ytimg.com/vi/08GR1_0Nflo/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLC3LDpLKiFTaeGmPjOtMSt7e1O3QA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Trudeau\'s%20Diversityathon.mp4',
                'genre': 'Misc'},
               {'name': 'FATHERLAND',
                'thumb': 'https://i.ytimg.com/vi/du1VW6n1Hvs/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLAfQMqevH8Ijpt0ugWLrtaHPAiIvA',
                'video': 'https://cheekyvideos.net/murdoch/videos/FATHERLAND.mp4',
                'genre': 'Misc'},
               {'name': 'They Sleep We Live',
                'thumb': 'https://i.ytimg.com/vi/czrv0-2b3i4/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLB4ben_PbEkt69oSHFei1Ix7vBRiw',
                'video': 'https://cheekyvideos.net/murdoch/videos/They%20Sleep,%20We%20Live.mp4',
                'genre': 'Misc'},
               {'name': 'No way San Jose',
                'thumb': 'https://i.ytimg.com/vi/tCfbeF8BT6k/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDu_pGt4NGmd6z45Gddoc4a_qUEzA',
                'video': 'https://cheekyvideos.net/murdoch/videos/No%20way,%20San%20Jose.mp4',
                'genre': 'Misc'},
               {'name': 'BREXIT',
                'thumb': 'https://i.ytimg.com/vi/Xk0Tm1-DDSE/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDTsnKxrB7IBPfAB-KwyuAFMvWMMw',
                'video': 'https://cheekyvideos.net/murdoch/videos/BREXIT.mp4',
                'genre': 'Misc'},
               {'name': 'Anti-Fascist Action',
                'thumb': 'https://i.ytimg.com/vi/ottANpOE2Nc/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBIRLL5GJWY-stX0w7kVy1_2r-oVA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Anti-Fascist%20Action.mp4',
                'genre': 'Misc'},
               {'name': 'Shameless Promotion for the NPI 2016 Fall Conference',
                'thumb': 'https://i.ytimg.com/vi/-4dKwOMlS78/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBmKMtP3ejswzFT63G5gQdOlKknNA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Shameless%20Promotion%20for%20the%20NPI%202016%20Fall%20Conference.mp4',
                'genre': 'Misc'},
               {'name': 'Obama\'s Legacy',
                'thumb': 'https://i.ytimg.com/vi/-4dKwOMlS78/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBmKMtP3ejswzFT63G5gQdOlKknNA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Obama\'s%20Legacy.mp4',
                'genre': 'Misc'},
               {'name': 'A Kangz Carol',
                'thumb': 'https://i.ytimg.com/vi/-4dKwOMlS78/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBmKMtP3ejswzFT63G5gQdOlKknNA',
                'video': 'https://cheekyvideos.net/murdoch/videos/A%20Kangz%20Carol.mp4',
                'genre': 'Misc'},
               {'name': 'Fatherland (Take 2)',
                'thumb': 'https://i.ytimg.com/vi/-4dKwOMlS78/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBmKMtP3ejswzFT63G5gQdOlKknNA',
                'video': 'https://cheekyvideos.net/murdoch/videos/Fatherland%20(Take%202).mp4',
                'genre': 'Misc'},
               {'name': 'The Greatest Generation',
                'thumb': 'https://i.ytimg.com/vi/-4dKwOMlS78/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBmKMtP3ejswzFT63G5gQdOlKknNA',
                'video': 'https://cheekyvideos.net/murdoch/videos/The%20Greatest%20Generation.mp4',
                'genre': 'Misc'},
              {'name': 'Immortality through delicious t shirt money',
                'thumb': 'https://i.ytimg.com/vi/LMZjJh2BHGs/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLCM88MVyM4b9dH-hhJj4coXTkmIZg',
                'video': 'https://cheekyvideos.net/murdoch/videos/Immortality%20through%20delicious%20t%20shirt%20money.mp4',
                'genre': 'Misc'}
               ]
          }

def get_url(**kwargs):

    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: list
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    #xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    #xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    xbmc.log('[Example Video Plugin] '  + sys.argv[2][1:], xbmc.LOGNOTICE)
    router(sys.argv[2][1:])
