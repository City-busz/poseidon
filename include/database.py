#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of Poseidon.
#
# Poseidon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Poseidon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Poseidon. If not, see <http://www.gnu.org/licenses/>.

import sys, requests, sqlite3 as lite
sys.path.append(".")
from functions import minify
from settings import autocomplete_policy, autocomplete_limit,\
history_con, bookmarks_con, cookies_con, verify_req

def autocomplete(query, liststore):

    if query:

        liststore.clear()

        if autocomplete_policy == 0:

            tmp = []
            tmp_ap = tmp.append

            with history_con:    
                history_cur = history_con.cursor()
                history_cur.execute("SELECT DISTINCT title,url FROM history LIMIT {};".format(autocomplete_limit))
                urls = history_cur.fetchall()

                if len(urls) != 0:
                    for url in urls:
                        tmp_ap(["{} | {}".format(minify(url[0], 50), minify(url[1], 100))] + [url[1]])

                for i in tmp: liststore.append(tuple(i))

            return True

        elif autocomplete_policy == 1:

            url = ("https://ac.duckduckgo.com/ac/?q={}&type=list".format(query))

            request = requests.get(url, stream=True, verify=verify_req)
            request = request.text.replace('[" ' + query + ' ",', "").replace("]", "").replace("[", "").replace('"', "").split(",")

            for i in request:
                if i: liststore.append([i])

            return True

def cookiesview():

    tmp = []
    cookies = []
    tmp_ap = tmp.append
    cookies_ap = cookies.append
        
    with cookies_con:    
        cookies_cur = cookies_con.cursor()
        cookies_cur.execute("SELECT * FROM moz_cookies;")
        cks = cookies_cur.fetchall()

        for i in cks:
            tmp_ap([i[0]] + [i[1]] + [minify(i[2],50)] + [i[3]] + [i[4]] +\
                   [i[5]] + [i[6]] + [i[7]] + [i[8]] + [i[2]])
        
        for i in tmp: cookies_ap(tuple(i))

        return cookies

def bookmarksview():

    tmp = []
    bookmarks = []
    tmp_ap = tmp.append
    bookmarks_ap = bookmarks.append
        
    with bookmarks_con:    
        bookmarks_cur = bookmarks_con.cursor()
        bookmarks_cur.execute("SELECT * FROM bookmarks ORDER BY date DESC;")
        urls = bookmarks_cur.fetchall()

        for i in urls: tmp_ap([i[2]] + [minify(i[0],50)] + [minify(i[1],50)] + [i[1]])
        for i in tmp: bookmarks_ap(tuple(i))

        return bookmarks

def historyview():

    tmp = []
    history = []
    tmp_ap = tmp.append
    history_ap = history.append
        
    with history_con:    
        history_cur = history_con.cursor()
        history_cur.execute("SELECT * FROM history ORDER BY date DESC;")
        urls = history_cur.fetchall()

        for i in urls: tmp_ap([i[2]] + [minify(i[0],50)] + [minify(i[1],50)] + [i[1]])
        for i in tmp: history_ap(tuple(i))

        return history

