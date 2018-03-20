
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ID CLASS HREF SRC TITLE LANG FINISH HTML BODY HEAD SECTION ASIDE ARTICLE NAV UL OL FOOTER HEADER TABLE LINK P H LI IMG TR TD TH CAPTION A TITLE_INITIAL BR HTML_FINISH BODY_FINISH HEAD_FINISH SECTION_FINISH ASIDE_FINISH ARTICLE_FINISH NAV_FINISH UL_FINISH OL_FINISH FOOTER_FINISH HEADER_FINISH TABLE_FINISH TITLE_FINISH P_FINISH H_FINISH LI_FINISH TR_FINISH TD_FINISH TH_FINISH CAPTION_FINISH A_FINISH TEXT VALUE EQUAL\n\tdoc : html_tag head body HTML_FINISH\n\t\n\thead : head_tag head_elements HEAD_FINISH\n\t\n\tbody : body_tag elements BODY_FINISH\n\t\n\tsection : section_tag elements SECTION_FINISH\n\t\n\taside : aside_tag elements ASIDE_FINISH\n\t\n\tarticle : article_tag elements ARTICLE_FINISH\n\t\n\tnav : nav_tag elements NAV_FINISH\n\t\n\tul : ul_tag list_elements UL_FINISH\n\t\n\tol : ol_tag list_elements OL_FINISH\n\t\n\tfooter : footer_tag elements FOOTER_FINISH\n\t\n\theader : header_tag elements HEADER_FINISH\n\t\n\ttable : table_tag table_elements TABLE_FINISH\n\t\n\ttr : tr_tag table_elements_basic TR_FINISH\n\t\n\ttitle : title_tag TEXT TITLE_FINISH\n\t\n\tlink : link_tag \n\t\n\tp : p_tag TEXT P_FINISH\n\t\n\th : h_tag TEXT H_FINISH\n\t\n\tli : li_tag TEXT LI_FINISH\n\t\n\timg : img_tag \n\t\n\ta : a_tag TEXT A_FINISH\n\t\n\tbr : br_tag \n\t\n\tth : th_tag TEXT TH_FINISH\n\t\n\ttd : td_tag TEXT TD_FINISH\n\t\n\tcaption : caption_tag TEXT CAPTION_FINISH\n\t\n\thtml_tag : HTML attributes FINISH\n\t\n\thead_tag : HEAD attributes FINISH\n\t\n\tbody_tag : BODY attributes FINISH\n\t\n\tsection_tag : SECTION attributes FINISH\n\t\n\taside_tag : ASIDE attributes FINISH\n\t\n\tarticle_tag : ARTICLE attributes FINISH\n\t\n\tnav_tag : NAV attributes FINISH\n\t\n\tul_tag : UL attributes FINISH\n\t\n\tol_tag : OL attributes FINISH\n\t\n\tfooter_tag : FOOTER attributes FINISH\n\t\n\theader_tag : HEADER attributes FINISH\n\t\n\ttable_tag : TABLE attributes FINISH\n\t\n\ttitle_tag : TITLE_INITIAL attributes FINISH\n\t\n\tlink_tag : LINK attributes FINISH\n\t\n\tp_tag : P attributes FINISH\n\t\n\th_tag : H attributes FINISH\n\t\n\tli_tag : LI attributes FINISH\n\t\n\timg_tag : IMG attributes FINISH\n\t\n\ttr_tag : TR attributes FINISH\n\t\n\ttd_tag : TD attributes FINISH\n\t\n\tth_tag : TH attributes FINISH\n\t\n\tcaption_tag : CAPTION attributes FINISH\n\t\n\ta_tag : A attributes FINISH\n\t\n\tbr_tag : BR \n\t\n\telements : empty\n\t\t\t| elements element\n\t\n\telement : section\n\t\t\t| aside\n\t\t\t| article\n\t\t\t| nav\n\t\t\t| ul\n\t\t\t| ol\n\t\t\t| footer\n\t\t\t| header\n\t\t\t| table\n\t\t\t| p\n\t\t\t| h\n\t\t\t| img\n\t\t\t| a\n\t\t\t| br\n\t\n\tlist_elements : empty\n\t\t\t\t| list_elements list_element\n\t\n\tlist_element : li\n\t\n\ttable_elements : empty\n\t\t\t\t| table_elements table_element\n\t\n\ttable_element : caption\n\t\t\t\t| tr\n\t\n\ttable_elements_basic : empty\n\t\t\t\t| table_elements_basic table_element_basic\n\t\n\ttable_element_basic : th\n\t\t\t\t\t\t| td\n\t\n\thead_elements : empty\n\t\t\t\t| head_elements head_element\n\t\n\thead_element : title\n\t\t\t\t| link\n\t\n\tattributes : empty  \n\t\t\t| attributes attribute\n\t\n\tattribute : ID EQUAL VALUE\n\t\t\t | CLASS EQUAL VALUE \n\t\t\t | HREF EQUAL VALUE\n\t\t\t | SRC EQUAL VALUE\n\t\t\t | TITLE EQUAL VALUE\n\t\t\t | LANG EQUAL VALUE\n\t\n\tempty : \n\t'
    
_lr_action_items = {'HTML':([0,],[3,]),'$end':([1,23,],[0,-1,]),'HEAD':([2,15,],[6,-25,]),'FINISH':([3,6,7,8,11,14,16,26,33,34,72,73,74,75,76,77,78,79,80,81,82,83,84,88,89,90,91,92,93,94,95,110,111,112,113,114,115,116,117,118,119,120,121,122,134,144,145,163,167,168,178,179,184,185,],[-88,-88,15,-80,-88,35,-81,86,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,124,125,-82,-83,-84,-85,-86,-87,149,150,151,152,153,154,155,156,157,158,159,160,161,-88,-88,-88,170,180,181,-88,-88,188,189,]),'ID':([3,6,7,8,11,14,16,26,33,34,72,73,74,75,76,77,78,79,80,81,82,83,84,88,89,90,91,92,93,94,95,110,111,112,113,114,115,116,117,118,119,120,121,122,134,144,145,163,167,168,178,179,184,185,],[-88,-88,17,-80,-88,17,-81,17,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,17,17,-82,-83,-84,-85,-86,-87,17,17,17,17,17,17,17,17,17,17,17,17,17,-88,-88,-88,17,17,17,-88,-88,17,17,]),'CLASS':([3,6,7,8,11,14,16,26,33,34,72,73,74,75,76,77,78,79,80,81,82,83,84,88,89,90,91,92,93,94,95,110,111,112,113,114,115,116,117,118,119,120,121,122,134,144,145,163,167,168,178,179,184,185,],[-88,-88,18,-80,-88,18,-81,18,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,18,18,-82,-83,-84,-85,-86,-87,18,18,18,18,18,18,18,18,18,18,18,18,18,-88,-88,-88,18,18,18,-88,-88,18,18,]),'HREF':([3,6,7,8,11,14,16,26,33,34,72,73,74,75,76,77,78,79,80,81,82,83,84,88,89,90,91,92,93,94,95,110,111,112,113,114,115,116,117,118,119,120,121,122,134,144,145,163,167,168,178,179,184,185,],[-88,-88,19,-80,-88,19,-81,19,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,19,19,-82,-83,-84,-85,-86,-87,19,19,19,19,19,19,19,19,19,19,19,19,19,-88,-88,-88,19,19,19,-88,-88,19,19,]),'SRC':([3,6,7,8,11,14,16,26,33,34,72,73,74,75,76,77,78,79,80,81,82,83,84,88,89,90,91,92,93,94,95,110,111,112,113,114,115,116,117,118,119,120,121,122,134,144,145,163,167,168,178,179,184,185,],[-88,-88,20,-80,-88,20,-81,20,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,20,20,-82,-83,-84,-85,-86,-87,20,20,20,20,20,20,20,20,20,20,20,20,20,-88,-88,-88,20,20,20,-88,-88,20,20,]),'TITLE':([3,6,7,8,11,14,16,26,33,34,72,73,74,75,76,77,78,79,80,81,82,83,84,88,89,90,91,92,93,94,95,110,111,112,113,114,115,116,117,118,119,120,121,122,134,144,145,163,167,168,178,179,184,185,],[-88,-88,21,-80,-88,21,-81,21,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,21,21,-82,-83,-84,-85,-86,-87,21,21,21,21,21,21,21,21,21,21,21,21,21,-88,-88,-88,21,21,21,-88,-88,21,21,]),'LANG':([3,6,7,8,11,14,16,26,33,34,72,73,74,75,76,77,78,79,80,81,82,83,84,88,89,90,91,92,93,94,95,110,111,112,113,114,115,116,117,118,119,120,121,122,134,144,145,163,167,168,178,179,184,185,],[-88,-88,22,-80,-88,22,-81,22,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,-88,22,22,-82,-83,-84,-85,-86,-87,22,22,22,22,22,22,22,22,22,22,22,22,22,-88,-88,-88,22,22,22,-88,-88,22,22,]),'BODY':([4,27,],[11,-2,]),'HEAD_FINISH':([5,12,13,28,29,30,32,35,123,125,],[-88,27,-76,-77,-78,-79,-15,-26,-14,-38,]),'TITLE_INITIAL':([5,12,13,28,29,30,32,35,123,125,],[-88,33,-76,-77,-78,-79,-15,-26,-14,-38,]),'LINK':([5,12,13,28,29,30,32,35,123,125,],[-88,34,-76,-77,-78,-79,-15,-26,-14,-38,]),'HTML_FINISH':([9,42,],[23,-3,]),'BODY_FINISH':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,69,71,85,86,126,127,128,129,130,135,136,137,138,146,147,148,160,],[-88,42,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-19,-21,-48,-27,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-42,]),'SECTION':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,72,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,72,72,72,72,72,72,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'ASIDE':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,73,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,73,73,73,73,73,73,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'ARTICLE':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,74,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,74,74,74,74,74,74,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'NAV':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,75,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,75,75,75,75,75,75,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'UL':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,76,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,76,76,76,76,76,76,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'OL':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,77,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,77,77,77,77,77,77,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'FOOTER':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,78,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,78,78,78,78,78,78,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'HEADER':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,79,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,79,79,79,79,79,79,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'TABLE':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,80,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,80,80,80,80,80,80,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'P':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,81,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,81,81,81,81,81,81,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'H':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,82,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,82,82,82,82,82,82,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'IMG':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,83,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,83,83,83,83,83,83,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'A':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,84,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,84,84,84,84,84,84,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'BR':([10,24,25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,69,71,85,86,96,97,98,99,103,104,126,127,128,129,130,135,136,137,138,146,147,148,149,150,151,152,155,156,160,],[-88,85,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-88,-88,-88,-88,-88,-19,-21,-48,-27,85,85,85,85,85,85,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-29,-30,-31,-34,-35,-42,]),'EQUAL':([17,18,19,20,21,22,],[36,37,38,39,40,41,]),'SECTION_FINISH':([25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,69,71,85,96,126,127,128,129,130,135,136,137,138,146,147,148,149,160,],[-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-19,-21,-48,126,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-28,-42,]),'ASIDE_FINISH':([25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,69,71,85,97,126,127,128,129,130,135,136,137,138,146,147,148,150,160,],[-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-19,-21,-48,127,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-29,-42,]),'ARTICLE_FINISH':([25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,69,71,85,98,126,127,128,129,130,135,136,137,138,146,147,148,151,160,],[-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-19,-21,-48,128,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-30,-42,]),'NAV_FINISH':([25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,61,69,71,85,99,126,127,128,129,130,135,136,137,138,146,147,148,152,160,],[-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-19,-21,-48,129,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-31,-42,]),'FOOTER_FINISH':([25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,64,69,71,85,103,126,127,128,129,130,135,136,137,138,146,147,148,155,160,],[-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-19,-21,-48,136,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-34,-42,]),'HEADER_FINISH':([25,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,65,69,71,85,104,126,127,128,129,130,135,136,137,138,146,147,148,156,160,],[-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-88,-19,-21,-48,137,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-20,-35,-42,]),'TEXT':([31,67,68,70,124,133,142,158,159,161,170,176,177,180,188,189,],[87,107,108,109,-37,162,164,-39,-40,-47,-41,182,183,-46,-45,-44,]),'VALUE':([36,37,38,39,40,41,],[90,91,92,93,94,95,]),'UL_FINISH':([62,100,101,131,132,153,169,],[-88,130,-65,-66,-67,-32,-18,]),'LI':([62,63,100,101,102,131,132,153,154,169,],[-88,-88,134,-65,134,-66,-67,-32,-33,-18,]),'OL_FINISH':([63,101,102,131,132,154,169,],[-88,-65,135,-66,-67,-33,-18,]),'TABLE_FINISH':([66,105,106,139,140,141,157,171,172,],[-88,138,-68,-69,-70,-71,-36,-24,-13,]),'CAPTION':([66,105,106,139,140,141,157,171,172,],[-88,144,-68,-69,-70,-71,-36,-24,-13,]),'TR':([66,105,106,139,140,141,157,171,172,],[-88,145,-68,-69,-70,-71,-36,-24,-13,]),'TITLE_FINISH':([87,],[123,]),'P_FINISH':([107,],[146,]),'H_FINISH':([108,],[147,]),'A_FINISH':([109,],[148,]),'TR_FINISH':([143,165,166,173,174,175,181,186,187,],[-88,172,-72,-73,-74,-75,-43,-22,-23,]),'TH':([143,165,166,173,174,175,181,186,187,],[-88,178,-72,-73,-74,-75,-43,-22,-23,]),'TD':([143,165,166,173,174,175,181,186,187,],[-88,179,-72,-73,-74,-75,-43,-22,-23,]),'LI_FINISH':([162,],[169,]),'CAPTION_FINISH':([164,],[171,]),'TH_FINISH':([182,],[186,]),'TD_FINISH':([183,],[187,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'doc':([0,],[1,]),'html_tag':([0,],[2,]),'head':([2,],[4,]),'head_tag':([2,],[5,]),'attributes':([3,6,11,33,34,72,73,74,75,76,77,78,79,80,81,82,83,84,134,144,145,178,179,],[7,14,26,88,89,110,111,112,113,114,115,116,117,118,119,120,121,122,163,167,168,184,185,]),'empty':([3,5,6,10,11,33,34,58,59,60,61,62,63,64,65,66,72,73,74,75,76,77,78,79,80,81,82,83,84,134,143,144,145,178,179,],[8,13,8,25,8,8,8,25,25,25,25,101,101,25,25,106,8,8,8,8,8,8,8,8,8,8,8,8,8,8,166,8,8,8,8,]),'body':([4,],[9,]),'body_tag':([4,],[10,]),'head_elements':([5,],[12,]),'attribute':([7,14,26,88,89,110,111,112,113,114,115,116,117,118,119,120,121,122,163,167,168,184,185,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'elements':([10,58,59,60,61,64,65,],[24,96,97,98,99,103,104,]),'head_element':([12,],[28,]),'title':([12,],[29,]),'link':([12,],[30,]),'title_tag':([12,],[31,]),'link_tag':([12,],[32,]),'element':([24,96,97,98,99,103,104,],[43,43,43,43,43,43,43,]),'section':([24,96,97,98,99,103,104,],[44,44,44,44,44,44,44,]),'aside':([24,96,97,98,99,103,104,],[45,45,45,45,45,45,45,]),'article':([24,96,97,98,99,103,104,],[46,46,46,46,46,46,46,]),'nav':([24,96,97,98,99,103,104,],[47,47,47,47,47,47,47,]),'ul':([24,96,97,98,99,103,104,],[48,48,48,48,48,48,48,]),'ol':([24,96,97,98,99,103,104,],[49,49,49,49,49,49,49,]),'footer':([24,96,97,98,99,103,104,],[50,50,50,50,50,50,50,]),'header':([24,96,97,98,99,103,104,],[51,51,51,51,51,51,51,]),'table':([24,96,97,98,99,103,104,],[52,52,52,52,52,52,52,]),'p':([24,96,97,98,99,103,104,],[53,53,53,53,53,53,53,]),'h':([24,96,97,98,99,103,104,],[54,54,54,54,54,54,54,]),'img':([24,96,97,98,99,103,104,],[55,55,55,55,55,55,55,]),'a':([24,96,97,98,99,103,104,],[56,56,56,56,56,56,56,]),'br':([24,96,97,98,99,103,104,],[57,57,57,57,57,57,57,]),'section_tag':([24,96,97,98,99,103,104,],[58,58,58,58,58,58,58,]),'aside_tag':([24,96,97,98,99,103,104,],[59,59,59,59,59,59,59,]),'article_tag':([24,96,97,98,99,103,104,],[60,60,60,60,60,60,60,]),'nav_tag':([24,96,97,98,99,103,104,],[61,61,61,61,61,61,61,]),'ul_tag':([24,96,97,98,99,103,104,],[62,62,62,62,62,62,62,]),'ol_tag':([24,96,97,98,99,103,104,],[63,63,63,63,63,63,63,]),'footer_tag':([24,96,97,98,99,103,104,],[64,64,64,64,64,64,64,]),'header_tag':([24,96,97,98,99,103,104,],[65,65,65,65,65,65,65,]),'table_tag':([24,96,97,98,99,103,104,],[66,66,66,66,66,66,66,]),'p_tag':([24,96,97,98,99,103,104,],[67,67,67,67,67,67,67,]),'h_tag':([24,96,97,98,99,103,104,],[68,68,68,68,68,68,68,]),'img_tag':([24,96,97,98,99,103,104,],[69,69,69,69,69,69,69,]),'a_tag':([24,96,97,98,99,103,104,],[70,70,70,70,70,70,70,]),'br_tag':([24,96,97,98,99,103,104,],[71,71,71,71,71,71,71,]),'list_elements':([62,63,],[100,102,]),'table_elements':([66,],[105,]),'list_element':([100,102,],[131,131,]),'li':([100,102,],[132,132,]),'li_tag':([100,102,],[133,133,]),'table_element':([105,],[139,]),'caption':([105,],[140,]),'tr':([105,],[141,]),'caption_tag':([105,],[142,]),'tr_tag':([105,],[143,]),'table_elements_basic':([143,],[165,]),'table_element_basic':([165,],[173,]),'th':([165,],[174,]),'td':([165,],[175,]),'th_tag':([165,],[176,]),'td_tag':([165,],[177,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> doc","S'",1,None,None,None),
  ('doc -> html_tag head body HTML_FINISH','doc',4,'p_doc_html','parser.py',14),
  ('head -> head_tag head_elements HEAD_FINISH','head',3,'p_head','parser.py',21),
  ('body -> body_tag elements BODY_FINISH','body',3,'p_body','parser.py',27),
  ('section -> section_tag elements SECTION_FINISH','section',3,'p_section','parser.py',33),
  ('aside -> aside_tag elements ASIDE_FINISH','aside',3,'p_aside','parser.py',39),
  ('article -> article_tag elements ARTICLE_FINISH','article',3,'p_article','parser.py',45),
  ('nav -> nav_tag elements NAV_FINISH','nav',3,'p_nav','parser.py',51),
  ('ul -> ul_tag list_elements UL_FINISH','ul',3,'p_ul','parser.py',57),
  ('ol -> ol_tag list_elements OL_FINISH','ol',3,'p_ol','parser.py',63),
  ('footer -> footer_tag elements FOOTER_FINISH','footer',3,'p_footer','parser.py',69),
  ('header -> header_tag elements HEADER_FINISH','header',3,'p_header','parser.py',75),
  ('table -> table_tag table_elements TABLE_FINISH','table',3,'p_table','parser.py',81),
  ('tr -> tr_tag table_elements_basic TR_FINISH','tr',3,'p_tr','parser.py',87),
  ('title -> title_tag TEXT TITLE_FINISH','title',3,'p_title','parser.py',94),
  ('link -> link_tag','link',1,'p_link','parser.py',100),
  ('p -> p_tag TEXT P_FINISH','p',3,'p_p','parser.py',106),
  ('h -> h_tag TEXT H_FINISH','h',3,'p_h','parser.py',112),
  ('li -> li_tag TEXT LI_FINISH','li',3,'p_li','parser.py',119),
  ('img -> img_tag','img',1,'p_img','parser.py',125),
  ('a -> a_tag TEXT A_FINISH','a',3,'p_a','parser.py',131),
  ('br -> br_tag','br',1,'p_br','parser.py',137),
  ('th -> th_tag TEXT TH_FINISH','th',3,'p_th','parser.py',143),
  ('td -> td_tag TEXT TD_FINISH','td',3,'p_td','parser.py',149),
  ('caption -> caption_tag TEXT CAPTION_FINISH','caption',3,'p_caption','parser.py',155),
  ('html_tag -> HTML attributes FINISH','html_tag',3,'p_html_tag','parser.py',165),
  ('head_tag -> HEAD attributes FINISH','head_tag',3,'p_head_tag','parser.py',171),
  ('body_tag -> BODY attributes FINISH','body_tag',3,'p_body_tag','parser.py',177),
  ('section_tag -> SECTION attributes FINISH','section_tag',3,'p_section_tag','parser.py',183),
  ('aside_tag -> ASIDE attributes FINISH','aside_tag',3,'p_aside_tag','parser.py',189),
  ('article_tag -> ARTICLE attributes FINISH','article_tag',3,'p_article_tag','parser.py',195),
  ('nav_tag -> NAV attributes FINISH','nav_tag',3,'p_nav_tag','parser.py',201),
  ('ul_tag -> UL attributes FINISH','ul_tag',3,'p_ul_tag','parser.py',207),
  ('ol_tag -> OL attributes FINISH','ol_tag',3,'p_ol_tag','parser.py',213),
  ('footer_tag -> FOOTER attributes FINISH','footer_tag',3,'p_footer_tag','parser.py',219),
  ('header_tag -> HEADER attributes FINISH','header_tag',3,'p_header_tag','parser.py',225),
  ('table_tag -> TABLE attributes FINISH','table_tag',3,'p_table_tag','parser.py',231),
  ('title_tag -> TITLE_INITIAL attributes FINISH','title_tag',3,'p_title_tag','parser.py',239),
  ('link_tag -> LINK attributes FINISH','link_tag',3,'p_link_tag','parser.py',245),
  ('p_tag -> P attributes FINISH','p_tag',3,'p_tag','parser.py',251),
  ('h_tag -> H attributes FINISH','h_tag',3,'p_h_tag','parser.py',257),
  ('li_tag -> LI attributes FINISH','li_tag',3,'p_li_tag','parser.py',264),
  ('img_tag -> IMG attributes FINISH','img_tag',3,'p_img_tag','parser.py',270),
  ('tr_tag -> TR attributes FINISH','tr_tag',3,'p_tr_tag','parser.py',276),
  ('td_tag -> TD attributes FINISH','td_tag',3,'p_td_tag','parser.py',282),
  ('th_tag -> TH attributes FINISH','th_tag',3,'p_th_tag','parser.py',288),
  ('caption_tag -> CAPTION attributes FINISH','caption_tag',3,'p_caption_tag','parser.py',294),
  ('a_tag -> A attributes FINISH','a_tag',3,'p_a_tag','parser.py',300),
  ('br_tag -> BR','br_tag',1,'p_br_tag','parser.py',306),
  ('elements -> empty','elements',1,'p_elements','parser.py',313),
  ('elements -> elements element','elements',2,'p_elements','parser.py',314),
  ('element -> section','element',1,'p_element','parser.py',324),
  ('element -> aside','element',1,'p_element','parser.py',325),
  ('element -> article','element',1,'p_element','parser.py',326),
  ('element -> nav','element',1,'p_element','parser.py',327),
  ('element -> ul','element',1,'p_element','parser.py',328),
  ('element -> ol','element',1,'p_element','parser.py',329),
  ('element -> footer','element',1,'p_element','parser.py',330),
  ('element -> header','element',1,'p_element','parser.py',331),
  ('element -> table','element',1,'p_element','parser.py',332),
  ('element -> p','element',1,'p_element','parser.py',333),
  ('element -> h','element',1,'p_element','parser.py',334),
  ('element -> img','element',1,'p_element','parser.py',335),
  ('element -> a','element',1,'p_element','parser.py',336),
  ('element -> br','element',1,'p_element','parser.py',337),
  ('list_elements -> empty','list_elements',1,'p_list_elements','parser.py',343),
  ('list_elements -> list_elements list_element','list_elements',2,'p_list_elements','parser.py',344),
  ('list_element -> li','list_element',1,'p_list_element','parser.py',354),
  ('table_elements -> empty','table_elements',1,'p_table_elements','parser.py',360),
  ('table_elements -> table_elements table_element','table_elements',2,'p_table_elements','parser.py',361),
  ('table_element -> caption','table_element',1,'p_table_element','parser.py',371),
  ('table_element -> tr','table_element',1,'p_table_element','parser.py',372),
  ('table_elements_basic -> empty','table_elements_basic',1,'p_table_elements_basic','parser.py',378),
  ('table_elements_basic -> table_elements_basic table_element_basic','table_elements_basic',2,'p_table_elements_basic','parser.py',379),
  ('table_element_basic -> th','table_element_basic',1,'p_table_element_basic','parser.py',389),
  ('table_element_basic -> td','table_element_basic',1,'p_table_element_basic','parser.py',390),
  ('head_elements -> empty','head_elements',1,'p_head_elements','parser.py',397),
  ('head_elements -> head_elements head_element','head_elements',2,'p_head_elements','parser.py',398),
  ('head_element -> title','head_element',1,'p_head_element','parser.py',408),
  ('head_element -> link','head_element',1,'p_head_element','parser.py',409),
  ('attributes -> empty','attributes',1,'p_attributes','parser.py',415),
  ('attributes -> attributes attribute','attributes',2,'p_attributes','parser.py',416),
  ('attribute -> ID EQUAL VALUE','attribute',3,'p_attribute','parser.py',426),
  ('attribute -> CLASS EQUAL VALUE','attribute',3,'p_attribute','parser.py',427),
  ('attribute -> HREF EQUAL VALUE','attribute',3,'p_attribute','parser.py',428),
  ('attribute -> SRC EQUAL VALUE','attribute',3,'p_attribute','parser.py',429),
  ('attribute -> TITLE EQUAL VALUE','attribute',3,'p_attribute','parser.py',430),
  ('attribute -> LANG EQUAL VALUE','attribute',3,'p_attribute','parser.py',431),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',453),
]
