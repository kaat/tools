# Random tools #

contact_convert.py — a tool to convert Contact files from Windows to a proper format with phone numbers. Improper files are results of exporting contacts from Iphone via Itunes. Improper .contact files have this to store phone number:

    <c:Extended><MSWABMAPI:PropTag0x800A001F c:type="string">+78001234567</MSWABMAPI:PropTag0x800A001F></c:Extended>
    
So Windows applications can't recognize this number ans don't show it. So these files can't be exported with native Windows tools.

vcf_encode.sh — supplementary tool to correct encoding of VCF files before importing them to Android.
