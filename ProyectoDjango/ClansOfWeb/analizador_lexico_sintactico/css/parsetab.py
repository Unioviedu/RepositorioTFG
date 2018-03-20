
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASTERISK COMA BRACKET_INITIAL BRACKET_FINISH CURLY_INITIAL CURLY_FINISH DASH GREATER_THAN HTML BODY HEAD SECTION ASIDE ARTICLE NAV UL OL FOOTER HEADER TABLE LINK P H LI IMG TR TD TH CAPTION A ID CLASS HREF SRC TITLE LANG MARGIN BORDER WIDTH PADDING TOP BOTTOM LEFT RIGHT HEIGHT BACKGROUND FONT SIZE COLOR COLUMNS VALUE EQUAL_TEXT POINT_TEXT HASHTAG_TEXT\n\tdoc : styles\n\t\n\tstyles : empty\n\t\t\t| styles style\n\t\n\tstyle : selectors BRACKET_INITIAL rules BRACKET_FINISH\n\t\n\trules : empty\n\t\t\t| rules rule\n\t\n\trule : MARGIN directions VALUE\n\t\t| BORDER DASH COLOR VALUE\n\t\t| BORDER DASH WIDTH VALUE\n\t\t| FONT DASH SIZE VALUE\n\t\t| FONT DASH COLOR VALUE\n\t\t| PADDING directions VALUE\n\t\t| HEIGHT VALUE\n\t\t| WIDTH VALUE\n\t\t| BACKGROUND VALUE\n\t\t| COLUMNS VALUE\n\t\n\tselectors : selector\n\t\t\t| selectors COMA selector\n\t\n\tselector : selector_universal \n\t\t\t| selector_type\n\t\t\t| selector_attribute \n\t\t\t| selector_class\n\t\t\t| selector_id\n\t\n\tselector_universal : ASTERISK\n\t\n\tselector_type : type\n\t\t\t| type GREATER_THAN type\n\t\n\tselector_attribute : CURLY_INITIAL attribute CURLY_FINISH\n\t\t\t\t\t| CURLY_INITIAL attribute EQUAL_TEXT CURLY_FINISH\n\t\t\t\t\t| type CURLY_INITIAL attribute CURLY_FINISH\n\t\t\t\t\t| type CURLY_INITIAL attribute EQUAL_TEXT CURLY_FINISH\n\t\n\tselector_class : POINT_TEXT\n\t\t\t\t| type POINT_TEXT\n\t\n\tselector_id : HASHTAG_TEXT\n\t\n\tdirections : empty\n\t\t\t| DASH TOP\n\t\t\t| DASH BOTTOM\n\t\t\t| DASH LEFT\n\t\t\t| DASH RIGHT\n\t\n\tid : ID\n\t\n\tclass : CLASS\n\t\n\thref : HREF\n\t\n\tsrc : SRC\n\t\n\tlang : LANG\n\t\n\thtml : HTML \n\t\n\thead : HEAD\n\t\n\tbody : BODY\n\t\n\tsection : SECTION\n\t\n\taside : ASIDE\n\t\n\tarticle : ARTICLE\n\t\n\tnav : NAV\n\t\n\tul : UL\n\t\n\tol : OL\n\t\n\tfooter : FOOTER\n\t\n\theader : HEADER\n\t\n\ttable : TABLE\n\t\n\ttr : TR\n\t\n\tlink : LINK\n\t\n\tp : P\n\t\n\th : H\n\t\n\tli : LI\n\t\n\timg : IMG \n\t\n\ta : A\n\t\n\tth : TH\n\t\n\ttd : TD\n\t\n\tcaption : CAPTION\n\t\n\tempty : \n\t\n\ttype : \t  html\t\n\t\t\t| body\n\t\t\t| head\n\t\t\t| section\n\t\t\t| aside\n\t\t\t| article\n\t\t\t| nav\n\t\t\t| ul\n\t\t\t| ol\n\t\t\t| footer\n\t\t\t| header\n\t\t\t| table\n\t\t\t| p\n\t\t\t| h\n\t\t\t| img\n\t\t\t| a\n\t\t\t| TITLE\n\t\t\t| link\n\t\t\t| th\n\t\t\t| td\n\t\t\t| tr\n\t\t\t| caption\n\t\t\t| li\n\t\n\tattribute : id\n\t\t\t | class \n\t\t\t | href\n\t\t\t | src\n\t\t\t | TITLE\n\t\t\t | lang\n\t'
    
_lr_action_items = {'ASTERISK':([0,2,3,4,63,86,],[-66,12,-2,-3,12,-4,]),'CURLY_INITIAL':([0,2,3,4,13,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,86,],[-66,14,-2,-3,65,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-44,-46,-45,-47,-48,-49,-50,-51,-52,-53,-54,-55,-58,-59,-61,-62,-57,-63,-64,-56,-65,-60,14,-4,]),'POINT_TEXT':([0,2,3,4,13,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,86,],[-66,15,-2,-3,66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-44,-46,-45,-47,-48,-49,-50,-51,-52,-53,-54,-55,-58,-59,-61,-62,-57,-63,-64,-56,-65,-60,15,-4,]),'HASHTAG_TEXT':([0,2,3,4,63,86,],[-66,16,-2,-3,16,-4,]),'TITLE':([0,2,3,4,14,63,64,65,86,],[-66,33,-2,-3,72,33,33,72,-4,]),'HTML':([0,2,3,4,63,64,86,],[-66,40,-2,-3,40,40,-4,]),'BODY':([0,2,3,4,63,64,86,],[-66,41,-2,-3,41,41,-4,]),'HEAD':([0,2,3,4,63,64,86,],[-66,42,-2,-3,42,42,-4,]),'SECTION':([0,2,3,4,63,64,86,],[-66,43,-2,-3,43,43,-4,]),'ASIDE':([0,2,3,4,63,64,86,],[-66,44,-2,-3,44,44,-4,]),'ARTICLE':([0,2,3,4,63,64,86,],[-66,45,-2,-3,45,45,-4,]),'NAV':([0,2,3,4,63,64,86,],[-66,46,-2,-3,46,46,-4,]),'UL':([0,2,3,4,63,64,86,],[-66,47,-2,-3,47,47,-4,]),'OL':([0,2,3,4,63,64,86,],[-66,48,-2,-3,48,48,-4,]),'FOOTER':([0,2,3,4,63,64,86,],[-66,49,-2,-3,49,49,-4,]),'HEADER':([0,2,3,4,63,64,86,],[-66,50,-2,-3,50,50,-4,]),'TABLE':([0,2,3,4,63,64,86,],[-66,51,-2,-3,51,51,-4,]),'P':([0,2,3,4,63,64,86,],[-66,52,-2,-3,52,52,-4,]),'H':([0,2,3,4,63,64,86,],[-66,53,-2,-3,53,53,-4,]),'IMG':([0,2,3,4,63,64,86,],[-66,54,-2,-3,54,54,-4,]),'A':([0,2,3,4,63,64,86,],[-66,55,-2,-3,55,55,-4,]),'LINK':([0,2,3,4,63,64,86,],[-66,56,-2,-3,56,56,-4,]),'TH':([0,2,3,4,63,64,86,],[-66,57,-2,-3,57,57,-4,]),'TD':([0,2,3,4,63,64,86,],[-66,58,-2,-3,58,58,-4,]),'TR':([0,2,3,4,63,64,86,],[-66,59,-2,-3,59,59,-4,]),'CAPTION':([0,2,3,4,63,64,86,],[-66,60,-2,-3,60,60,-4,]),'LI':([0,2,3,4,63,64,86,],[-66,61,-2,-3,61,61,-4,]),'$end':([0,1,2,3,4,86,],[-66,0,-1,-2,-3,-4,]),'BRACKET_INITIAL':([5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,81,82,84,96,98,109,],[62,-17,-19,-20,-21,-22,-23,-24,-25,-31,-33,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-44,-46,-45,-47,-48,-49,-50,-51,-52,-53,-54,-55,-58,-59,-61,-62,-57,-63,-64,-56,-65,-60,-32,-18,-26,-27,-29,-28,-30,]),'COMA':([5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,81,82,84,96,98,109,],[63,-17,-19,-20,-21,-22,-23,-24,-25,-31,-33,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-44,-46,-45,-47,-48,-49,-50,-51,-52,-53,-54,-55,-58,-59,-61,-62,-57,-63,-64,-56,-65,-60,-32,-18,-26,-27,-29,-28,-30,]),'GREATER_THAN':([13,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[64,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-44,-46,-45,-47,-48,-49,-50,-51,-52,-53,-54,-55,-58,-59,-61,-62,-57,-63,-64,-56,-65,-60,]),'ID':([14,65,],[74,74,]),'CLASS':([14,65,],[75,75,]),'HREF':([14,65,],[76,76,]),'SRC':([14,65,],[77,77,]),'LANG':([14,65,],[78,78,]),'BRACKET_FINISH':([62,79,80,87,103,106,107,108,110,119,120,121,122,123,],[-66,86,-5,-6,-14,-13,-15,-16,-7,-12,-8,-9,-10,-11,]),'MARGIN':([62,79,80,87,103,106,107,108,110,119,120,121,122,123,],[-66,88,-5,-6,-14,-13,-15,-16,-7,-12,-8,-9,-10,-11,]),'BORDER':([62,79,80,87,103,106,107,108,110,119,120,121,122,123,],[-66,89,-5,-6,-14,-13,-15,-16,-7,-12,-8,-9,-10,-11,]),'FONT':([62,79,80,87,103,106,107,108,110,119,120,121,122,123,],[-66,91,-5,-6,-14,-13,-15,-16,-7,-12,-8,-9,-10,-11,]),'PADDING':([62,79,80,87,103,106,107,108,110,119,120,121,122,123,],[-66,92,-5,-6,-14,-13,-15,-16,-7,-12,-8,-9,-10,-11,]),'HEIGHT':([62,79,80,87,103,106,107,108,110,119,120,121,122,123,],[-66,93,-5,-6,-14,-13,-15,-16,-7,-12,-8,-9,-10,-11,]),'WIDTH':([62,79,80,87,102,103,106,107,108,110,119,120,121,122,123,],[-66,90,-5,-6,116,-14,-13,-15,-16,-7,-12,-8,-9,-10,-11,]),'BACKGROUND':([62,79,80,87,103,106,107,108,110,119,120,121,122,123,],[-66,94,-5,-6,-14,-13,-15,-16,-7,-12,-8,-9,-10,-11,]),'COLUMNS':([62,79,80,87,103,106,107,108,110,119,120,121,122,123,],[-66,95,-5,-6,-14,-13,-15,-16,-7,-12,-8,-9,-10,-11,]),'CURLY_FINISH':([67,68,69,70,71,72,73,74,75,76,77,78,83,85,97,],[84,-90,-91,-92,-93,-94,-95,-39,-40,-41,-42,-43,96,98,109,]),'EQUAL_TEXT':([67,68,69,70,71,72,73,74,75,76,77,78,83,],[85,-90,-91,-92,-93,-94,-95,-39,-40,-41,-42,-43,97,]),'DASH':([88,89,91,92,],[101,102,104,101,]),'VALUE':([88,90,92,93,94,95,99,100,105,111,112,113,114,115,116,117,118,],[-66,103,-66,106,107,108,110,-34,119,-35,-36,-37,-38,120,121,122,123,]),'TOP':([101,],[111,]),'BOTTOM':([101,],[112,]),'LEFT':([101,],[113,]),'RIGHT':([101,],[114,]),'COLOR':([102,104,],[115,118,]),'SIZE':([104,],[117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'doc':([0,],[1,]),'styles':([0,],[2,]),'empty':([0,62,88,92,],[3,80,100,100,]),'style':([2,],[4,]),'selectors':([2,],[5,]),'selector':([2,63,],[6,81,]),'selector_universal':([2,63,],[7,7,]),'selector_type':([2,63,],[8,8,]),'selector_attribute':([2,63,],[9,9,]),'selector_class':([2,63,],[10,10,]),'selector_id':([2,63,],[11,11,]),'type':([2,63,64,],[13,13,82,]),'html':([2,63,64,],[17,17,17,]),'body':([2,63,64,],[18,18,18,]),'head':([2,63,64,],[19,19,19,]),'section':([2,63,64,],[20,20,20,]),'aside':([2,63,64,],[21,21,21,]),'article':([2,63,64,],[22,22,22,]),'nav':([2,63,64,],[23,23,23,]),'ul':([2,63,64,],[24,24,24,]),'ol':([2,63,64,],[25,25,25,]),'footer':([2,63,64,],[26,26,26,]),'header':([2,63,64,],[27,27,27,]),'table':([2,63,64,],[28,28,28,]),'p':([2,63,64,],[29,29,29,]),'h':([2,63,64,],[30,30,30,]),'img':([2,63,64,],[31,31,31,]),'a':([2,63,64,],[32,32,32,]),'link':([2,63,64,],[34,34,34,]),'th':([2,63,64,],[35,35,35,]),'td':([2,63,64,],[36,36,36,]),'tr':([2,63,64,],[37,37,37,]),'caption':([2,63,64,],[38,38,38,]),'li':([2,63,64,],[39,39,39,]),'attribute':([14,65,],[67,83,]),'id':([14,65,],[68,68,]),'class':([14,65,],[69,69,]),'href':([14,65,],[70,70,]),'src':([14,65,],[71,71,]),'lang':([14,65,],[73,73,]),'rules':([62,],[79,]),'rule':([79,],[87,]),'directions':([88,92,],[99,105,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> doc","S'",1,None,None,None),
  ('doc -> styles','doc',1,'p_doc_css','parser.py',17),
  ('styles -> empty','styles',1,'p_styles','parser.py',25),
  ('styles -> styles style','styles',2,'p_styles','parser.py',26),
  ('style -> selectors BRACKET_INITIAL rules BRACKET_FINISH','style',4,'p_style','parser.py',37),
  ('rules -> empty','rules',1,'p_rules','parser.py',45),
  ('rules -> rules rule','rules',2,'p_rules','parser.py',46),
  ('rule -> MARGIN directions VALUE','rule',3,'p_rule','parser.py',56),
  ('rule -> BORDER DASH COLOR VALUE','rule',4,'p_rule','parser.py',57),
  ('rule -> BORDER DASH WIDTH VALUE','rule',4,'p_rule','parser.py',58),
  ('rule -> FONT DASH SIZE VALUE','rule',4,'p_rule','parser.py',59),
  ('rule -> FONT DASH COLOR VALUE','rule',4,'p_rule','parser.py',60),
  ('rule -> PADDING directions VALUE','rule',3,'p_rule','parser.py',61),
  ('rule -> HEIGHT VALUE','rule',2,'p_rule','parser.py',62),
  ('rule -> WIDTH VALUE','rule',2,'p_rule','parser.py',63),
  ('rule -> BACKGROUND VALUE','rule',2,'p_rule','parser.py',64),
  ('rule -> COLUMNS VALUE','rule',2,'p_rule','parser.py',65),
  ('selectors -> selector','selectors',1,'p_selectors','parser.py',86),
  ('selectors -> selectors COMA selector','selectors',3,'p_selectors','parser.py',87),
  ('selector -> selector_universal','selector',1,'p_selector','parser.py',98),
  ('selector -> selector_type','selector',1,'p_selector','parser.py',99),
  ('selector -> selector_attribute','selector',1,'p_selector','parser.py',100),
  ('selector -> selector_class','selector',1,'p_selector','parser.py',101),
  ('selector -> selector_id','selector',1,'p_selector','parser.py',102),
  ('selector_universal -> ASTERISK','selector_universal',1,'p_selector_universal','parser.py',110),
  ('selector_type -> type','selector_type',1,'p_selector_type','parser.py',116),
  ('selector_type -> type GREATER_THAN type','selector_type',3,'p_selector_type','parser.py',117),
  ('selector_attribute -> CURLY_INITIAL attribute CURLY_FINISH','selector_attribute',3,'p_selector_attribute','parser.py',126),
  ('selector_attribute -> CURLY_INITIAL attribute EQUAL_TEXT CURLY_FINISH','selector_attribute',4,'p_selector_attribute','parser.py',127),
  ('selector_attribute -> type CURLY_INITIAL attribute CURLY_FINISH','selector_attribute',4,'p_selector_attribute','parser.py',128),
  ('selector_attribute -> type CURLY_INITIAL attribute EQUAL_TEXT CURLY_FINISH','selector_attribute',5,'p_selector_attribute','parser.py',129),
  ('selector_class -> POINT_TEXT','selector_class',1,'p_selector_class','parser.py',145),
  ('selector_class -> type POINT_TEXT','selector_class',2,'p_selector_class','parser.py',146),
  ('selector_id -> HASHTAG_TEXT','selector_id',1,'p_selector_id','parser.py',157),
  ('directions -> empty','directions',1,'p_directions','parser.py',164),
  ('directions -> DASH TOP','directions',2,'p_directions','parser.py',165),
  ('directions -> DASH BOTTOM','directions',2,'p_directions','parser.py',166),
  ('directions -> DASH LEFT','directions',2,'p_directions','parser.py',167),
  ('directions -> DASH RIGHT','directions',2,'p_directions','parser.py',168),
  ('id -> ID','id',1,'p_id','parser.py',179),
  ('class -> CLASS','class',1,'p_class','parser.py',185),
  ('href -> HREF','href',1,'p_href','parser.py',191),
  ('src -> SRC','src',1,'p_src','parser.py',197),
  ('lang -> LANG','lang',1,'p_lang','parser.py',204),
  ('html -> HTML','html',1,'p_html_tag','parser.py',210),
  ('head -> HEAD','head',1,'p_head','parser.py',216),
  ('body -> BODY','body',1,'p_body','parser.py',222),
  ('section -> SECTION','section',1,'p_section','parser.py',228),
  ('aside -> ASIDE','aside',1,'p_aside','parser.py',234),
  ('article -> ARTICLE','article',1,'p_article','parser.py',240),
  ('nav -> NAV','nav',1,'p_nav','parser.py',246),
  ('ul -> UL','ul',1,'p_ul','parser.py',252),
  ('ol -> OL','ol',1,'p_ol','parser.py',258),
  ('footer -> FOOTER','footer',1,'p_footer','parser.py',264),
  ('header -> HEADER','header',1,'p_header','parser.py',270),
  ('table -> TABLE','table',1,'p_table','parser.py',276),
  ('tr -> TR','tr',1,'p_tr','parser.py',282),
  ('link -> LINK','link',1,'p_link','parser.py',288),
  ('p -> P','p',1,'p_p','parser.py',294),
  ('h -> H','h',1,'p_h','parser.py',300),
  ('li -> LI','li',1,'p_li','parser.py',307),
  ('img -> IMG','img',1,'p_img','parser.py',313),
  ('a -> A','a',1,'p_a','parser.py',319),
  ('th -> TH','th',1,'p_th','parser.py',325),
  ('td -> TD','td',1,'p_td','parser.py',331),
  ('caption -> CAPTION','caption',1,'p_caption','parser.py',337),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',343),
  ('type -> html','type',1,'p_type','parser.py',349),
  ('type -> body','type',1,'p_type','parser.py',350),
  ('type -> head','type',1,'p_type','parser.py',351),
  ('type -> section','type',1,'p_type','parser.py',352),
  ('type -> aside','type',1,'p_type','parser.py',353),
  ('type -> article','type',1,'p_type','parser.py',354),
  ('type -> nav','type',1,'p_type','parser.py',355),
  ('type -> ul','type',1,'p_type','parser.py',356),
  ('type -> ol','type',1,'p_type','parser.py',357),
  ('type -> footer','type',1,'p_type','parser.py',358),
  ('type -> header','type',1,'p_type','parser.py',359),
  ('type -> table','type',1,'p_type','parser.py',360),
  ('type -> p','type',1,'p_type','parser.py',361),
  ('type -> h','type',1,'p_type','parser.py',362),
  ('type -> img','type',1,'p_type','parser.py',363),
  ('type -> a','type',1,'p_type','parser.py',364),
  ('type -> TITLE','type',1,'p_type','parser.py',365),
  ('type -> link','type',1,'p_type','parser.py',366),
  ('type -> th','type',1,'p_type','parser.py',367),
  ('type -> td','type',1,'p_type','parser.py',368),
  ('type -> tr','type',1,'p_type','parser.py',369),
  ('type -> caption','type',1,'p_type','parser.py',370),
  ('type -> li','type',1,'p_type','parser.py',371),
  ('attribute -> id','attribute',1,'p_attribute','parser.py',379),
  ('attribute -> class','attribute',1,'p_attribute','parser.py',380),
  ('attribute -> href','attribute',1,'p_attribute','parser.py',381),
  ('attribute -> src','attribute',1,'p_attribute','parser.py',382),
  ('attribute -> TITLE','attribute',1,'p_attribute','parser.py',383),
  ('attribute -> lang','attribute',1,'p_attribute','parser.py',384),
]
