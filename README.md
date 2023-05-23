# FB_OpenRedirect
Facebook open-redirection vulnerability with linkshim hash capturing 

Summary
What is an open-redirection attack?
Open redirection vulnerabilities arise when an application allows users to
command redirects, or forward to external URLs. With the help of an open redirection
vulnerability, attackers can redirect ignorant users from a valid domain to a malicious
site, for example a phishing website.
For example, the following url is an open redirection URL,
https://facebook.com/l.php?u=https://example.com
Open redirection adds validity to phishing attacks. Victims are deceived to see the
legitimate, trusted domains (facebook.com) in the above example, overseeing the
redirection to the phished website.
What is the Facebook link shim system?
The main objective of Link Shim is to verify if the external link you are accessing
from Facebook is malicious. It will check Facebook's internal list of malicious links and
the external partners' lists (McAfee, Google, Web of Trust, and Websense). If they find
the destination domain suspicious, they redirect the user to an intermediate notification
page, which notifies the user about the external redirection, and asks them if they want
to return to Facebook or continue with the redirection. The redirection to the destination
domain occurs automatically.
The redirection notice page looks like this,
The red highlighted part in the following URL is an example of a link shim hash,
“https://l.facebook.com/l.php?u=https%3A%2F%2Fyoutu.be%2FKuQoQgL63Xo%3Ffbclid%3DIw
AR0em7YPvefXbZe7X2_mqC2NbNJW1NpQX1Y0VDVhb5b5ppa0FA6WVcQ9S28&h=AT1FDPer
uKHpXt3y86955ZA1-CLj8g8VqJmYhVmnkzVyzfGTFEglxPsTmBwnLyuPX_4ok6-kWrBvv4Lr
35ZArdRjDKuTEO5SBB7jg6srUXIVupCbdZmVjlhHPpz2gNTSlpB5&__tn__=-UK-R&c[0]=AT2
1W1KHSk40Fgwu1_Gsf_p1jnptwP81OrnJqrb_34PIq7F9kB1c_Z3XKeex0tmEG8DV5nnyz3pj
6U7DNeVfb81UJrsaghpXqs0RXT3G3Uzti1XBZCLq2xeY5JdH6NnNzEkxWtO7rnQHrVkqOUi
PXsNIVGcr5DoGZVgZY4s_-_RcXCPQYTNynTICaxXZ “
2.Methodology
The Vulnerability
Unfortunately, in the case of facebook, these linkshim hashes can be captured.
Once a valid linkshim hash is attached to the end of a redirection URL as a parameter, it
gives legitimacy to the redirection, bypassing the redirect notice page. However, this
vulnerability would not work with sites that are already blocked by facebook.
The linkshim hash capturing can be done using selenium and a few string
functions. I've prepared a code using Selenium with Python that saves all redirection
URLs from a facebook page, captures the linkshim hash from a particular redirection
URL, and concatenates the linkshim hash to my illegitimate facebook redirection URL,
as a parameter, giving my redirection URL a validity.
Following are a few code snippets and the outputs obtained,
Proof of Concept 1:
Above code snippet captures all the links on a facebook page and saves them in a
dictionary called “link_list”. Hence, it sorts out the redirection URLs from that dictionary
by checking if the string “l.php” is present or not, and saves the latest redirection URL
in another string called “red_list”. In this way, I've retrieved the latest redirection URL
from a particular facebook page.
Proof Of Concept 2:
The following code snippet highlights the capturing of the linkshim hash. The
latest redirection URL stored in the string “red_list” is divided into two parts.
● str1: This string stores the URL up to the “l.php?u=” endpoint.
● str2: This string stores the linkshim hash as a “&h” parameter.
Proof Of Concept 3:
Finally, the code concatenates the source domain (facebook.com), the destination
domain and the linkshim hash together, providing with a legitimate redirection URL as
an output, that bypasses the redirection notice. The result is as follows,
The redirection URL obtained from facebook page:
https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2Fyoutube&h=AT0nCrrbT1QxlYG
XQ60np3BWRNz5qeZ15hTBKXDBxm6Y_8ZlRHEv4e98UJLf15aQkib-_z_F8rpdEKHOZWamLPQEY1Om
JTxoEZTBVXtafyYLFbPpWOkrAv1-o28GWxShzt1Qjzslmnwpc1StDmwseE84UG62PE672ss
The legitimate URL obtained after linkshim capturing:
https://l.facebook.com/l.php?u=https://example.com/&h=AT0nCrrbT1QxlYGXQ60np3BWRNz5qeZ15hTB
KXDBxm6Y_8ZlRHEv4e98UJLf15aQkib-_z_F8rpdEKHOZWamLPQEY1OmJTxoEZTBVXtafyYLFbPpWO
krAv1-o28GWxShzt1Qjzslmnwpc1StDmwseE84UG62PE672ss
Notice how the linkshim hash beginning from &h is the same for both URLs.
Note: The linkshim hash expires after a certain amount of time. To execute the
redirection successfully, the code has to be executed regularly to obtain the latest
linkshim hash everytime.
Conclusion:
Hence, open redirect attacks on facebook are possible, maybe not for phishing emails
due to the time limitations but maybe for a phishing attack on social media, chats, live
streams, etc.
About the author:
Arjun Ghoshal is an Computer Science Engineering sophomore from the Institute of
Engineering and Management, based in Kolkata,India. He takes great interest in the
field of cybersecurity and is willing to make more of such contributions in the future.
