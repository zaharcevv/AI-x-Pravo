# test.summarizer.py

from scraper.summarizer import summarize_html_content

from scraper.summarizer import get_client, summarize_html_content

client = get_client(api_key="sk-Ec8tjnWYqcxqQBk4k9IE1A")
html_content = """
<html xmlns="http://www.w3.org/1999/xhtml" style="height: 100%; text-size-adjust: auto;"><!-- CONVEX # converter_version:9.17.0 # generated_on:20260225-1121 # ELI version:0.2 --><head><meta name="format-detection" content="telephone=no"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="WT.z_usr_lan" content="EN">
   <meta http-equiv="content-type" content="text/html; charset=utf-8">
   <script type="text/javascript" src="/eurlex-frontoffice/ruxitagentjs_ICANVfgqrux_10327251022105625.js" data-dtconfig="app=47d4c64c3b67ec69|agentId=e7e1ebf011e1e375|owasp=1|featureHash=ICANVfgqrux|rdnt=1|uxrgce=1|cuc=m097nmfl|mel=100000|mb=null|dpvc=1|iub=null|lastModification=1772705312123|tp=500,50,0|srbbv=2|agentUri=/eurlex-frontoffice/ruxitagentjs_ICANVfgqrux_10327251022105625.js|reportUrl=/eurlex-frontoffice/rb_39a3e95b-5423-482c-879b-99ef235dffeb|rid=RID_679777279|rpid=-703196648|domain=europa.eu"></script><style type="text/css" id="operaUserStyle"></style><link type="text/css" rel="stylesheet" href="./../../../../css/oj/oj-convex-act.css">
   <title>L_202600454EN.000101.fmx.xml</title>
<link rel="canonical" href="https://eur-lex.europa.eu/eli/dec/2026/454/oj/eng">
<link rel="stylesheet" media="all" href="./../../../../revamp/components/vendor/bootstrap/dist/css/bootstrap.css"><link rel="stylesheet" media="all" href="./../../../../revamp/components/vendor/font-awesome/css/font-awesome.min.css"><link rel="stylesheet" media="all" href="./../../../../revamp/css/eurlex.css"><link rel="stylesheet" media="all" href="./../../../../revamp/css/eurlex-dev.css"><link rel="stylesheet" media="all" href="./../../../../css/oj/oj.css"></head>
<body style="margin: 0px;"><div class="Wrapper clearfix" style="max-width: none;"><div class="container-fluid"><div class="row row-offcanvas"><div class="col-md-3" id="TOC"><div id="TOCSidebarWrapper"><div class="affix" id="TOCSidebarSA" style="width: 827px;"><div class="tocWrapper"><button class="fa fa-times" id="tocHideBtnStandalone" type="button" onclick="hideTOC($(&quot;.tocWrapper&quot;));" aria-hidden="true" style="visibility: visible;"></button><nav class="toc-sidebar" style=""><ul id="TOC_docHtml" class="toc-eli-subdivisions nav toc-sidenav" style=""><li><a href="#tit_1"><span class="toc-eli-label">DECISION (EU) …</span></a></li><li><a href="#pbl_1"><i class="fa fa-angle-right"></i>preamble</a><ul class="nav collapse"><li><a href="#cit_1">citation</a></li><li><a href="#rct_1">recital 1</a></li><li><a href="#rct_2">recital 2</a></li><li><a href="#rct_3">recital 3</a></li><li><a href="#rct_4">recital 4</a></li><li><a href="#rct_5">recital 5</a></li></ul></li><li><a style="font-weight:500;" href="#enc_1"><i class="fa fa-angle-right"></i>enacting terms</a><ul class="nav collapse"><li><a style="font-weight:500;" href="#art_1">article 1</a></li><li><a style="font-weight:500;" href="#art_2">article 2</a></li></ul></li><li><a href="#fnp_1">Concluding formulas</a></li></ul></nav></div></div></div></div><div id="docHtml" class="col-md-9" style="padding-bottom: 169px;">
   <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <colgroup><col width="5%">
      <col width="75%">
      <col width="20%">
      </colgroup><tbody>
         <tr>
            <td>
               <img alt="European flag" src="./../../../../images/europeanflag.gif" height="40pt" width="60pt">
            </td>
            <td>
               <p class="oj-hd-ti">Official Journal <br>of the European Union</p>
            </td>
            <td>
               <p class="oj-hd-lg">EN</p>
               <p class="oj-hd-coll">L series</p>
            </td>
         </tr>
      </tbody>
   </table>
   <hr class="oj-separator">
   <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <colgroup><col width="20%">
      <col width="60%">
      <col width="20%">
      </colgroup><tbody>
         <tr>
            <td>
            </td><td>
               <p class="oj-hd-uniq">2026/454</p>
            </td>
            <td>
               <p class="oj-hd-date">4.3.2026</p>
            </td>
         </tr>
      </tbody>
   </table>
   <div class="eli-container">
      <div class="eli-main-title" id="tit_1">
         <p class="oj-doc-ti" id="d1e38-1-1">
            DECISION (EU) 2026/454 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL
         </p>
         <p class="oj-doc-ti">of 17&nbsp;February 2026
         </p>
         <p class="oj-doc-ti">on the mobilisation of the European Globalisation Adjustment Fund for Displaced Workers following an application from Belgium&nbsp;– EGF/2025/006 BE/Audi</p>
      </div>
      <div class="eli-subdivision" id="pbl_1">
         <p class="oj-normal">THE EUROPEAN PARLIAMENT AND THE COUNCIL OF THE EUROPEAN UNION,</p>
         <div class="eli-subdivision" id="cit_1">
            <p class="oj-normal">Having regard to the Treaty on the Functioning of the European Union,</p>
         </div>
         <div class="eli-subdivision" id="cit_2">
            <p class="oj-normal">Having regard to Regulation (EU) 2021/691 of the European Parliament and of the Council of 28&nbsp;April 2021 on the European Globalisation Adjustment Fund for Displaced Workers (EGF) and repealing Regulation (EU) No&nbsp;1309/2013&nbsp;<a id="ntc1-L_202600454EN.000101-E0001" href="#ntr1-L_202600454EN.000101-E0001">(<span class="oj-super oj-note-tag">1</span>)</a>, and in particular Article&nbsp;15(1), first subparagraph, thereof,</p>
         </div>
         <div class="eli-subdivision" id="cit_3">
            <p class="oj-normal">Having regard to the Interinstitutional Agreement of 16&nbsp;December 2020 between the European Parliament, the Council of the European Union and the European Commission on budgetary discipline, on cooperation in budgetary matters and on sound financial management, as well as on new own resources, including a&nbsp;roadmap towards the introduction of new own resources&nbsp;<a id="ntc2-L_202600454EN.000101-E0002" href="#ntr2-L_202600454EN.000101-E0002">(<span class="oj-super oj-note-tag">2</span>)</a>, and in particular point 9 thereof,</p>
         </div>
         <div class="eli-subdivision" id="cit_4">
            <p class="oj-normal">Having regard to the proposal from the European Commission,</p>
         </div>
         <p class="oj-normal">Whereas:</p>
         <div class="eli-subdivision" id="rct_1">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
               <colgroup><col width="4%">
               <col width="96%">
               </colgroup><tbody>
                  <tr>
                     <td valign="top">
                        <p class="oj-normal">(1)</p>
                     </td>
                     <td valign="top">
                        <p class="oj-normal">The European Globalisation Adjustment Fund for Displaced Workers (EGF) aims to demonstrate solidarity and promote decent and sustainable employment in the Union by providing support for workers made redundant and self-employed persons whose activity has ceased in the case of major restructuring events and assisting them in returning to decent and sustainable employment as soon as possible.</p>
                     </td>
                  </tr>
               </tbody>
            </table>
         </div>
         <div class="eli-subdivision" id="rct_2">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
               <colgroup><col width="4%">
               <col width="96%">
               </colgroup><tbody>
                  <tr>
                     <td valign="top">
                        <p class="oj-normal">(2)</p>
                     </td>
                     <td valign="top">
                        <p class="oj-normal">The EGF is not to exceed a&nbsp;maximum annual amount of EUR 30&nbsp;million (in 2018 prices), as laid down in Article&nbsp;8 of Council Regulation (EU, Euratom) 2020/2093&nbsp;<a id="ntc3-L_202600454EN.000101-E0003" href="#ntr3-L_202600454EN.000101-E0003">(<span class="oj-super oj-note-tag">3</span>)</a> amended by Council Regulation (EU, Euratom) 2024/765&nbsp;<a id="ntc4-L_202600454EN.000101-E0004" href="#ntr4-L_202600454EN.000101-E0004">(<span class="oj-super oj-note-tag">4</span>)</a>, and Article&nbsp;16 of Regulation (EU) 2021/691.</p>
                     </td>
                  </tr>
               </tbody>
            </table>
         </div>
         <div class="eli-subdivision" id="rct_3">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
               <colgroup><col width="4%">
               <col width="96%">
               </colgroup><tbody>
                  <tr>
                     <td valign="top">
                        <p class="oj-normal">(3)</p>
                     </td>
                     <td valign="top">
                        <p class="oj-normal">On 18&nbsp;September 2025, Belgium submitted an application to mobilise the EGF in accordance with Article&nbsp;8(1) of Regulation (EU) 2021/691, in respect of workers’ displacements in Audi Brussels S.A.: n.V. and five of its suppliers and downstream producers in Belgium. It was supplemented by additional information provided in accordance with Article&nbsp;8(5) of Regulation (EU) 2021/691. That application is considered to comply with the conditions for providing a&nbsp;financial contribution from the EGF as laid down in Article&nbsp;13 of Regulation (EU) 2021/691, on the basis of the assessment made by the Commission in the Proposal for a&nbsp;mobilisation decision of the European Parliament and of the Council&nbsp;<a id="ntc5-L_202600454EN.000101-E0005" href="#ntr5-L_202600454EN.000101-E0005">(<span class="oj-super oj-note-tag">5</span>)</a>.</p>
                     </td>
                  </tr>
               </tbody>
            </table>
         </div>
         <div class="eli-subdivision" id="rct_4">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
               <colgroup><col width="4%">
               <col width="96%">
               </colgroup><tbody>
                  <tr>
                     <td valign="top">
                        <p class="oj-normal">(4)</p>
                     </td>
                     <td valign="top">
                        <p class="oj-normal">The EGF should, therefore, be mobilised to provide a&nbsp;financial contribution of EUR 7&nbsp;527&nbsp;625 in respect of the application submitted by Belgium.</p>
                     </td>
                  </tr>
               </tbody>
            </table>
         </div>
         <div class="eli-subdivision" id="rct_5">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
               <colgroup><col width="4%">
               <col width="96%">
               </colgroup><tbody>
                  <tr>
                     <td valign="top">
                        <p class="oj-normal">(5)</p>
                     </td>
                     <td valign="top">
                        <p class="oj-normal">In order to minimise the time taken to mobilise the EGF, this Decision should apply from the date of its adoption,</p>
                     </td>
                  </tr>
               </tbody>
            </table>
         </div>
         <p class="oj-normal">HAVE ADOPTED THIS DECISION:</p>
      </div>
      <div class="eli-subdivision" id="enc_1">
         <div class="eli-subdivision" id="art_1">
            <p id="d1e156-1-1" class="oj-ti-art">Article&nbsp;1</p>
            <p class="oj-normal">For the general budget of the Union for the financial year 2026, the European Globalisation Adjustment Fund for Displaced Workers shall be mobilised to provide the amount of EUR 7&nbsp;527&nbsp;625 in commitment and payment appropriations.</p>
         </div>
         <div class="eli-subdivision" id="art_2">
            <p id="d1e164-1-1" class="oj-ti-art">Article&nbsp;2</p>
            <p class="oj-normal">This Decision shall enter into force on the day of its publication in the <span class="oj-italic">Official Journal of the European Union</span>.</p>
            <p class="oj-normal">It shall apply from 17&nbsp;February 2026.</p>
         </div>
      </div>
      <div class="eli-subdivision" id="fnp_1">
         <div class="oj-final">
            <p class="oj-normal">Done at Brussels, 17&nbsp;February 2026.</p>
            <div class="oj-signatory">
               <p class="oj-signatory">
                  <span class="oj-italic">For the European Parliament</span>
               </p>
               <p class="oj-signatory">
                  <span class="oj-italic">The President</span>
               </p>
               <p class="oj-signatory">R. METSOLA
            </p>
            </div>
            <div class="oj-signatory">
               <p class="oj-signatory">
                  <span class="oj-italic">For the Council</span>
               </p>
               <p class="oj-signatory">
                  <span class="oj-italic">The President</span>
               </p>
               <p class="oj-signatory">M. KERAVNOS
            </p>
            </div>
         </div>
      </div>
      <hr class="oj-note">
      <p class="oj-note">
         <a id="ntr1-L_202600454EN.000101-E0001" href="#ntc1-L_202600454EN.000101-E0001">(<span class="oj-super">1</span>)</a>&nbsp;&nbsp;
            <a href="./../../../../legal-content/EN/AUTO/?uri=OJ:L:2021:153:TOC">OJ L&nbsp;153, 3.5.2021, p.&nbsp;48</a>, ELI: <a href="http://data.europa.eu/eli/reg/2021/691/oj">http://data.europa.eu/eli/reg/2021/691/oj</a>.</p>
      <p class="oj-note">
         <a id="ntr2-L_202600454EN.000101-E0002" href="#ntc2-L_202600454EN.000101-E0002">(<span class="oj-super">2</span>)</a>&nbsp;&nbsp;
            <a href="./../../../../legal-content/EN/AUTO/?uri=OJ:L:2020:433I:TOC">OJ L&nbsp;433&nbsp;I, 22.12.2020, p.&nbsp;28</a>, ELI: <a href="http://data.europa.eu/eli/agree_interinstit/2020/1222/oj">http://data.europa.eu/eli/agree_interinstit/2020/1222/oj</a>.</p>
      <p class="oj-note">
         <a id="ntr3-L_202600454EN.000101-E0003" href="#ntc3-L_202600454EN.000101-E0003">(<span class="oj-super">3</span>)</a>&nbsp;&nbsp;Council Regulation (EU, Euratom) 2020/2093 of 17&nbsp;December 2020 laying down the multiannual financial framework for the years 2021 to 2027 (<a href="./../../../../legal-content/EN/AUTO/?uri=OJ:L:2020:433I:TOC">OJ L&nbsp;433&nbsp;I, 22.12.2020, p.&nbsp;11</a>, ELI: <a href="http://data.europa.eu/eli/reg/2020/2093/oj">http://data.europa.eu/eli/reg/2020/2093/oj</a>).</p>
      <p class="oj-note">
         <a id="ntr4-L_202600454EN.000101-E0004" href="#ntc4-L_202600454EN.000101-E0004">(<span class="oj-super">4</span>)</a>&nbsp;&nbsp;Council Regulation (EU, Euratom) 2024/765 of 29&nbsp;February 2024 amending Regulation (EU, Euratom) 2020/2093 laying down the multiannual financial framework for the years 2021 to 2027 (<a href="https://data.europa.eu/eli/reg/2024/765/oj">OJ&nbsp;L, 2024/765, 29.2.2024, ELI:&nbsp;http://data.europa.eu/eli/reg/2024/765/oj</a>).</p>
      <p class="oj-note">
         <a id="ntr5-L_202600454EN.000101-E0005" href="#ntc5-L_202600454EN.000101-E0005">(<span class="oj-super">5</span>)</a>&nbsp;&nbsp;COM(2026) 2.</p>
   </div>
   <hr class="oj-separator">
   <p class="oj-normal">ELI: http://data.europa.eu/eli/dec/2026/454/oj</p>
   <p class="oj-normal">ISSN 1977-0677 (electronic edition)</p>
   <hr class="oj-doc-end">
<script src="./../../../../js/jquery.js">//</script><script src="./../../../../dynamic-js/eli_subdivisions_en.js">//</script><script src="./../../../../dynamic-js/config.js">//</script><script src="./../../../../dynamic-js/const.js">//</script><script src="./../../../../js/TOC_ELI_SUBDIVISIONS.js">//</script><script src="./../../../../revamp/components/vendor/bootstrap/dist/js/bootstrap.min.js">//</script><script src="./../../../../revamp/js/metisMenu.min.js">//</script><script src="./../../../../revamp/js/eurlex.js">//</script><script src="./../../../../js/eur-lex-sanitizer.js">//</script><script src="./../../../../js/eur-lex.js">//</script><script src="./../../../../js/cookieConsentKitUtils.js?v=2.18.4">//</script><script src="./../../../../js/TOC.js">//</script><script type="text/javascript">$(document).ready(function(){generateTOC(true,'', 'Top','false');scrollToCurrentUrlAnchor();});</script>

</div></div></div></div></body></html>
"""

# Summarize
summary = summarize_html_content(html_content, client)

# Print result
print("SUMMARY:\n", summary)