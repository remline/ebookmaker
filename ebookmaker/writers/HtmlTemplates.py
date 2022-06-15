#!/usr/bin/env python
#  -*- mode: python; indent-tabs-mode: nil; -*- coding: utf-8 -*-

"""
HtmlTemplates.py

Copyright 2022 by Project Gutenberg

Use f-strings to render boilerplate trees
"""
import html
import lxml
from lxml import etree

def pgheader(dc):
    def pstyle(key, val):
        if not val:
            return ''
        return f"<p style='display:block; margin-top:1em; margin-bottom:1em; margin-left:2em; text-indent:-2em'><strong>{key}</strong>: {html.escape(val)}</p>"

    language_list = []
    lang = ''
    for language in dc.languages:
        lang = lang if lang else language.id 
        language_list.append(language.language)

    if 'copyright' in dc.rights:
        rights = 'This is a *copyrighted* Project Gutenberg eBook, details below.'
    else:
        rights = '''
This ebook is for the use of anyone anywhere in the United States and most other parts of the world at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the <a class="reference internal" href="#project-gutenberg-license">Project Gutenberg License</a> included with this ebook or online at <a class="reference external" href="https://www.gutenberg.org/license">https://www.gutenberg.org/license</a>. If you are not located in the United States, you’ll have to check the laws of the country where you are located before using this eBook.'''

    pg_header = f'''
<section class="pg-boilerplate pgheader" id="pg-header" xml:lang="en" lang="en" xmlns="http://www.w3.org/1999/xhtml">
    <h2 style='text-align:center; font-size:1.2em; font-weight:bold'>The Project Gutenberg eBook of <span lang='{lang}' xml:lang='{lang}'>{html.escape(dc.title_no_subtitle)}</span>, by {html.escape(dc.authors_short())}</h2>
    <div style='display:block; margin:1em 0'>{rights}</div>

    <div class="container" id="pg-machine-header">
        {pstyle('Title', dc.title_no_subtitle)}
        {pstyle('Subtitle', dc.subtitle)}
        {pstyle('Author', dc.authors_short())}
        {pstyle('Release Date', 
            f'{dc.release_date.strftime("%B %-d, %Y")} [EBook #{dc.project_gutenberg_id}]')}
        {pstyle('Language', ', '.join(language_list))}
        {pstyle('Original Publication', dc.pubinfo)}
        {pstyle('Credits', dc.credit)}
    </div>
    <div class="vspace" style="height: 2em"><br /></div>
        <div style="text-align:center">
            <span>*** START OF THIS PROJECT GUTENBERG EBOOK ***</span>
        </div>
</section>
'''
    return etree.fromstring(pg_header, lxml.html.XHTMLParser())
    

def pgfooter(dc):
    copyright_addition = '''<p>This particular work is one of the few individual works protected
by copyright law in the United States and most of the remainder of the
world, included in the Project Gutenberg collection with the
permission of the copyright holder. Information on the copyright owner
for this particular work and the terms of use imposed by the copyright
holder on this work are set forth at the beginning of this work.</p>
    ''' if 'copyright' in dc.rights else ''

    pg_footer = f'''
<section class="pg-boilerplate pgheader" id="pg-footer" lang='en' xml:lang='en' xmlns="http://www.w3.org/1999/xhtml">
        <div style="text-align:center">
            <span>*** END OF THIS PROJECT GUTENBERG EBOOK ***</span>
        </div>

<div style='display:block; margin:1em 0'>
Updated editions will replace the previous one&#8212;the old editions will
be renamed.
</div>

<div style='display:block; margin:1em 0'>
Creating the works from print editions not protected by U.S. copyright
law means that no one owns a United States copyright in these works,
so the Foundation (and you!) can copy and distribute it in the United
States without permission and without paying copyright
royalties. Special rules, set forth in the General Terms of Use part
of this license, apply to copying and distributing Project
Gutenberg&#8482; electronic works to protect the PROJECT GUTENBERG&#8482;
concept and trademark. Project Gutenberg is a registered trademark,
and may not be used if you charge for an eBook, except by following
the terms of the trademark license, including paying royalties for use
of the Project Gutenberg trademark. If you do not charge anything for
copies of this eBook, complying with the trademark license is very
easy. You may use this eBook for nearly any purpose such as creation
of derivative works, reports, performances and research. Project
Gutenberg eBooks may be modified and printed and given away&#8212;you may
do practically ANYTHING in the United States with eBooks not protected
by U.S. copyright law. Redistribution is subject to the trademark
license, especially commercial redistribution.
</div>

<div style='margin-top:1em; font-size:1.1em; text-align:center' id='project-gutenberg-license'>START: FULL LICENSE</div>
<h2 style='text-align:center;font-size:0.9em'>THE FULL PROJECT GUTENBERG LICENSE</h2>
<div style='text-align:center;font-size:0.9em'>PLEASE READ THIS BEFORE YOU DISTRIBUTE OR USE THIS WORK</div>

<div style='display:block; margin:1em 0'>
To protect the Project Gutenberg&#8482; mission of promoting the free
distribution of electronic works, by using or distributing this work
(or any other work associated in any way with the phrase &#8220;Project
Gutenberg&#8221;), you agree to comply with all the terms of the Full
Project Gutenberg&#8482; License available with this file or online at
www.gutenberg.org/license.
</div>

<div style='display:block; font-size:1.1em; margin:1em 0; font-weight:bold'>
Section 1. General Terms of Use and Redistributing Project Gutenberg&#8482; electronic works
</div>

<div style='display:block; margin:1em 0'>
1.A. By reading or using any part of this Project Gutenberg&#8482;
electronic work, you indicate that you have read, understand, agree to
and accept all the terms of this license and intellectual property
(trademark/copyright) agreement. If you do not agree to abide by all
the terms of this agreement, you must cease using and return or
destroy all copies of Project Gutenberg&#8482; electronic works in your
possession. If you paid a fee for obtaining a copy of or access to a
Project Gutenberg&#8482; electronic work and you do not agree to be bound
by the terms of this agreement, you may obtain a refund from the person
or entity to whom you paid the fee as set forth in paragraph 1.E.8.
</div>

<div style='display:block; margin:1em 0'>
1.B. &#8220;Project Gutenberg&#8221; is a registered trademark. It may only be
used on or associated in any way with an electronic work by people who
agree to be bound by the terms of this agreement. There are a few
things that you can do with most Project Gutenberg&#8482; electronic works
even without complying with the full terms of this agreement. See
paragraph 1.C below. There are a lot of things you can do with Project
Gutenberg&#8482; electronic works if you follow the terms of this
agreement and help preserve free future access to Project Gutenberg&#8482;
electronic works. See paragraph 1.E below.
</div>

<div style='display:block; margin:1em 0'>
1.C. The Project Gutenberg Literary Archive Foundation (&#8220;the
Foundation&#8221; or PGLAF), owns a compilation copyright in the collection
of Project Gutenberg&#8482; electronic works. Nearly all the individual
works in the collection are in the public domain in the United
States. If an individual work is unprotected by copyright law in the
United States and you are located in the United States, we do not
claim a right to prevent you from copying, distributing, performing,
displaying or creating derivative works based on the work as long as
all references to Project Gutenberg are removed. Of course, we hope
that you will support the Project Gutenberg&#8482; mission of promoting
free access to electronic works by freely sharing Project Gutenberg&#8482;
works in compliance with the terms of this agreement for keeping the
Project Gutenberg&#8482; name associated with the work. You can easily
comply with the terms of this agreement by keeping this work in the
same format with its attached full Project Gutenberg&#8482; License when
you share it without charge with others.
</div>

{copyright_addition}
<div style='display:block; margin:1em 0'>
1.D. The copyright laws of the place where you are located also govern
what you can do with this work. Copyright laws in most countries are
in a constant state of change. If you are outside the United States,
check the laws of your country in addition to the terms of this
agreement before downloading, copying, displaying, performing,
distributing or creating derivative works based on this work or any
other Project Gutenberg&#8482; work. The Foundation makes no
representations concerning the copyright status of any work in any
country other than the United States.
</div>

<div style='display:block; margin:1em 0'>
1.E. Unless you have removed all references to Project Gutenberg:
</div>

<div style='display:block; margin:1em 0'>
1.E.1. The following sentence, with active links to, or other
immediate access to, the full Project Gutenberg&#8482; License must appear
prominently whenever any copy of a Project Gutenberg&#8482; work (any work
on which the phrase &#8220;Project Gutenberg&#8221; appears, or with which the
phrase &#8220;Project Gutenberg&#8221; is associated) is accessed, displayed,
performed, viewed, copied or distributed:
</div>

<blockquote>
  <div style='display:block; margin:1em 0'>
    This eBook is for the use of anyone anywhere in the United States and most
    other parts of the world at no cost and with almost no restrictions
    whatsoever. You may copy it, give it away or re-use it under the terms
    of the Project Gutenberg License included with this eBook or online
    at <a href="https://www.gutenberg.org">www.gutenberg.org</a>. If you
    are not located in the United States, you will have to check the laws
    of the country where you are located before using this eBook.
  </div>
</blockquote>

<div style='display:block; margin:1em 0'>
1.E.2. If an individual Project Gutenberg&#8482; electronic work is
derived from texts not protected by U.S. copyright law (does not
contain a notice indicating that it is posted with permission of the
copyright holder), the work can be copied and distributed to anyone in
the United States without paying any fees or charges. If you are
redistributing or providing access to a work with the phrase &#8220;Project
Gutenberg&#8221; associated with or appearing on the work, you must comply
either with the requirements of paragraphs 1.E.1 through 1.E.7 or
obtain permission for the use of the work and the Project Gutenberg&#8482;
trademark as set forth in paragraphs 1.E.8 or 1.E.9.
</div>

<div style='display:block; margin:1em 0'>
1.E.3. If an individual Project Gutenberg&#8482; electronic work is posted
with the permission of the copyright holder, your use and distribution
must comply with both paragraphs 1.E.1 through 1.E.7 and any
additional terms imposed by the copyright holder. Additional terms
will be linked to the Project Gutenberg&#8482; License for all works
posted with the permission of the copyright holder found at the
beginning of this work.
</div>

<div style='display:block; margin:1em 0'>
1.E.4. Do not unlink or detach or remove the full Project Gutenberg&#8482;
License terms from this work, or any files containing a part of this
work or any other work associated with Project Gutenberg&#8482;.
</div>

<div style='display:block; margin:1em 0'>
1.E.5. Do not copy, display, perform, distribute or redistribute this
electronic work, or any part of this electronic work, without
prominently displaying the sentence set forth in paragraph 1.E.1 with
active links or immediate access to the full terms of the Project
Gutenberg&#8482; License.
</div>

<div style='display:block; margin:1em 0'>
1.E.6. You may convert to and distribute this work in any binary,
compressed, marked up, nonproprietary or proprietary form, including
any word processing or hypertext form. However, if you provide access
to or distribute copies of a Project Gutenberg&#8482; work in a format
other than &#8220;Plain Vanilla ASCII&#8221; or other format used in the official
version posted on the official Project Gutenberg&#8482; website
(www.gutenberg.org), you must, at no additional cost, fee or expense
to the user, provide a copy, a means of exporting a copy, or a means
of obtaining a copy upon request, of the work in its original &#8220;Plain
Vanilla ASCII&#8221; or other form. Any alternate format must include the
full Project Gutenberg&#8482; License as specified in paragraph 1.E.1.
</div>

<div style='display:block; margin:1em 0'>
1.E.7. Do not charge a fee for access to, viewing, displaying,
performing, copying or distributing any Project Gutenberg&#8482; works
unless you comply with paragraph 1.E.8 or 1.E.9.
</div>

<div style='display:block; margin:1em 0'>
1.E.8. You may charge a reasonable fee for copies of or providing
access to or distributing Project Gutenberg&#8482; electronic works
provided that:
</div>

<div style='margin-left:0.7em;'>
    <div style='text-indent:-0.7em'>
        &#8226; You pay a royalty fee of 20% of the gross profits you derive from
        the use of Project Gutenberg&#8482; works calculated using the method
        you already use to calculate your applicable taxes. The fee is owed
        to the owner of the Project Gutenberg&#8482; trademark, but he has
        agreed to donate royalties under this paragraph to the Project
        Gutenberg Literary Archive Foundation. Royalty payments must be paid
        within 60 days following each date on which you prepare (or are
        legally required to prepare) your periodic tax returns. Royalty
        payments should be clearly marked as such and sent to the Project
        Gutenberg Literary Archive Foundation at the address specified in
        Section 4, &#8220;Information about donations to the Project Gutenberg
        Literary Archive Foundation.&#8221;
    </div>

    <div style='text-indent:-0.7em'>
        &#8226; You provide a full refund of any money paid by a user who notifies
        you in writing (or by e-mail) within 30 days of receipt that s/he
        does not agree to the terms of the full Project Gutenberg&#8482;
        License. You must require such a user to return or destroy all
        copies of the works possessed in a physical medium and discontinue
        all use of and all access to other copies of Project Gutenberg&#8482;
        works.
    </div>

    <div style='text-indent:-0.7em'>
        &#8226; You provide, in accordance with paragraph 1.F.3, a full refund of
        any money paid for a work or a replacement copy, if a defect in the
        electronic work is discovered and reported to you within 90 days of
        receipt of the work.
    </div>

    <div style='text-indent:-0.7em'>
        &#8226; You comply with all other terms of this agreement for free
        distribution of Project Gutenberg&#8482; works.
    </div>
</div>

<div style='display:block; margin:1em 0'>
1.E.9. If you wish to charge a fee or distribute a Project
Gutenberg&#8482; electronic work or group of works on different terms than
are set forth in this agreement, you must obtain permission in writing
from the Project Gutenberg Literary Archive Foundation, the manager of
the Project Gutenberg&#8482; trademark. Contact the Foundation as set
forth in Section 3 below.
</div>

<div style='display:block; margin:1em 0'>
1.F.
</div>

<div style='display:block; margin:1em 0'>
1.F.1. Project Gutenberg volunteers and employees expend considerable
effort to identify, do copyright research on, transcribe and proofread
works not protected by U.S. copyright law in creating the Project
Gutenberg&#8482; collection. Despite these efforts, Project Gutenberg&#8482;
electronic works, and the medium on which they may be stored, may
contain &#8220;Defects,&#8221; such as, but not limited to, incomplete, inaccurate
or corrupt data, transcription errors, a copyright or other
intellectual property infringement, a defective or damaged disk or
other medium, a computer virus, or computer codes that damage or
cannot be read by your equipment.
</div>

<div style='display:block; margin:1em 0'>
1.F.2. LIMITED WARRANTY, DISCLAIMER OF DAMAGES - Except for the &#8220;Right
of Replacement or Refund&#8221; described in paragraph 1.F.3, the Project
Gutenberg Literary Archive Foundation, the owner of the Project
Gutenberg&#8482; trademark, and any other party distributing a Project
Gutenberg&#8482; electronic work under this agreement, disclaim all
liability to you for damages, costs and expenses, including legal
fees. YOU AGREE THAT YOU HAVE NO REMEDIES FOR NEGLIGENCE, STRICT
LIABILITY, BREACH OF WARRANTY OR BREACH OF CONTRACT EXCEPT THOSE
PROVIDED IN PARAGRAPH 1.F.3. YOU AGREE THAT THE FOUNDATION, THE
TRADEMARK OWNER, AND ANY DISTRIBUTOR UNDER THIS AGREEMENT WILL NOT BE
LIABLE TO YOU FOR ACTUAL, DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE OR
INCIDENTAL DAMAGES EVEN IF YOU GIVE NOTICE OF THE POSSIBILITY OF SUCH
DAMAGE.
</div>

<div style='display:block; margin:1em 0'>
1.F.3. LIMITED RIGHT OF REPLACEMENT OR REFUND - If you discover a
defect in this electronic work within 90 days of receiving it, you can
receive a refund of the money (if any) you paid for it by sending a
written explanation to the person you received the work from. If you
received the work on a physical medium, you must return the medium
with your written explanation. The person or entity that provided you
with the defective work may elect to provide a replacement copy in
lieu of a refund. If you received the work electronically, the person
or entity providing it to you may choose to give you a second
opportunity to receive the work electronically in lieu of a refund. If
the second copy is also defective, you may demand a refund in writing
without further opportunities to fix the problem.
</div>

<div style='display:block; margin:1em 0'>
1.F.4. Except for the limited right of replacement or refund set forth
in paragraph 1.F.3, this work is provided to you &#8216;AS-IS&#8217;, WITH NO
OTHER WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO WARRANTIES OF MERCHANTABILITY OR FITNESS FOR ANY PURPOSE.
</div>

<div style='display:block; margin:1em 0'>
1.F.5. Some states do not allow disclaimers of certain implied
warranties or the exclusion or limitation of certain types of
damages. If any disclaimer or limitation set forth in this agreement
violates the law of the state applicable to this agreement, the
agreement shall be interpreted to make the maximum disclaimer or
limitation permitted by the applicable state law. The invalidity or
unenforceability of any provision of this agreement shall not void the
remaining provisions.
</div>

<div style='display:block; margin:1em 0'>
1.F.6. INDEMNITY - You agree to indemnify and hold the Foundation, the
trademark owner, any agent or employee of the Foundation, anyone
providing copies of Project Gutenberg&#8482; electronic works in
accordance with this agreement, and any volunteers associated with the
production, promotion and distribution of Project Gutenberg&#8482;
electronic works, harmless from all liability, costs and expenses,
including legal fees, that arise directly or indirectly from any of
the following which you do or cause to occur: (a) distribution of this
or any Project Gutenberg&#8482; work, (b) alteration, modification, or
additions or deletions to any Project Gutenberg&#8482; work, and (c) any
Defect you cause.
</div>

<div style='display:block; font-size:1.1em; margin:1em 0; font-weight:bold'>
Section 2. Information about the Mission of Project Gutenberg&#8482;
</div>

<div style='display:block; margin:1em 0'>
Project Gutenberg&#8482; is synonymous with the free distribution of
electronic works in formats readable by the widest variety of
computers including obsolete, old, middle-aged and new computers. It
exists because of the efforts of hundreds of volunteers and donations
from people in all walks of life.
</div>

<div style='display:block; margin:1em 0'>
Volunteers and financial support to provide volunteers with the
assistance they need are critical to reaching Project Gutenberg&#8482;&#8217;s
goals and ensuring that the Project Gutenberg&#8482; collection will
remain freely available for generations to come. In 2001, the Project
Gutenberg Literary Archive Foundation was created to provide a secure
and permanent future for Project Gutenberg&#8482; and future
generations. To learn more about the Project Gutenberg Literary
Archive Foundation and how your efforts and donations can help, see
Sections 3 and 4 and the Foundation information page at www.gutenberg.org.
</div>

<div style='display:block; font-size:1.1em; margin:1em 0; font-weight:bold'>
Section 3. Information about the Project Gutenberg Literary Archive Foundation
</div>

<div style='display:block; margin:1em 0'>
The Project Gutenberg Literary Archive Foundation is a non-profit
501(c)(3) educational corporation organized under the laws of the
state of Mississippi and granted tax exempt status by the Internal
Revenue Service. The Foundation&#8217;s EIN or federal tax identification
number is 64-6221541. Contributions to the Project Gutenberg Literary
Archive Foundation are tax deductible to the full extent permitted by
U.S. federal laws and your state&#8217;s laws.
</div>

<div style='display:block; margin:1em 0'>
The Foundation&#8217;s business office is located at 809 North 1500 West,
Salt Lake City, UT 84116, (801) 596-1887. Email contact links and up
to date contact information can be found at the Foundation&#8217;s website
and official page at www.gutenberg.org/contact
</div>

<div style='display:block; font-size:1.1em; margin:1em 0; font-weight:bold'>
Section 4. Information about Donations to the Project Gutenberg Literary Archive Foundation
</div>

<div style='display:block; margin:1em 0'>
Project Gutenberg&#8482; depends upon and cannot survive without widespread
public support and donations to carry out its mission of
increasing the number of public domain and licensed works that can be
freely distributed in machine-readable form accessible by the widest
array of equipment including outdated equipment. Many small donations
($1 to $5,000) are particularly important to maintaining tax exempt
status with the IRS.
</div>

<div style='display:block; margin:1em 0'>
The Foundation is committed to complying with the laws regulating
charities and charitable donations in all 50 states of the United
States. Compliance requirements are not uniform and it takes a
considerable effort, much paperwork and many fees to meet and keep up
with these requirements. We do not solicit donations in locations
where we have not received written confirmation of compliance. To SEND
DONATIONS or determine the status of compliance for any particular state
visit <a href="https://www.gutenberg.org/donate/">www.gutenberg.org/donate</a>.
</div>

<div style='display:block; margin:1em 0'>
While we cannot and do not solicit contributions from states where we
have not met the solicitation requirements, we know of no prohibition
against accepting unsolicited donations from donors in such states who
approach us with offers to donate.
</div>

<div style='display:block; margin:1em 0'>
International donations are gratefully accepted, but we cannot make
any statements concerning tax treatment of donations received from
outside the United States. U.S. laws alone swamp our small staff.
</div>

<div style='display:block; margin:1em 0'>
Please check the Project Gutenberg web pages for current donation
methods and addresses. Donations are accepted in a number of other
ways including checks, online payments and credit card donations. To
donate, please visit: www.gutenberg.org/donate
</div>

<div style='display:block; font-size:1.1em; margin:1em 0; font-weight:bold'>
Section 5. General Information About Project Gutenberg&#8482; electronic works
</div>

<div style='display:block; margin:1em 0'>
Professor Michael S. Hart was the originator of the Project
Gutenberg&#8482; concept of a library of electronic works that could be
freely shared with anyone. For forty years, he produced and
distributed Project Gutenberg&#8482; eBooks with only a loose network of
volunteer support.
</div>

<div style='display:block; margin:1em 0'>
Project Gutenberg&#8482; eBooks are often created from several printed
editions, all of which are confirmed as not protected by copyright in
the U.S. unless a copyright notice is included. Thus, we do not
necessarily keep eBooks in compliance with any particular paper
edition.
</div>

<div style='display:block; margin:1em 0'>
Most people start at our website which has the main PG search
facility: <a href="https://www.gutenberg.org">www.gutenberg.org</a>.
</div>

<div style='display:block; margin:1em 0'>
This website includes information about Project Gutenberg&#8482;,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.
</div>

</section>
'''
    return etree.fromstring(pg_footer, lxml.html.XHTMLParser())