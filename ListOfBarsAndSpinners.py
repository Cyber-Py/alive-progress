'''
List of bars:
classic = standard_bar_factory(borders='[]')
classic2 = standard_bar_factory(background='.', chars='#', borders='[]', tip='')
smooth = standard_bar_factory(chars='▏▎▍▌▋▊▉█', tip=None, errors='⚠✗')
blocks = standard_bar_factory(chars='▏▎▍▌▋▊▉', tip=None, errors='⚠✗')
bubbles = standard_bar_factory(chars='∙○⦿●', borders='<>', tip='', errors='⚠✗')
circles = standard_bar_factory(background='○', chars='●', borders='<>', tip='', 
errors='⚠✗')
hollow = standard_bar_factory(chars='❒', borders='<>', tip='▷', errors='⚠✗')
squares = standard_bar_factory(background='❒', chars='■', borders='<>', tip='', 
errors='⚠✗')
solid = standard_bar_factory(chars='■', borders='<>', tip='►', errors='⚠✗')
checks = standard_bar_factory(chars='✓', tip='', errors='⚠✗')
filling = standard_bar_factory(chars='▁▂▃▄▅▆▇█', tip=None, errors='⚠✗')
'''
########################################################################
'''
List of spinners:
classic = frame_spinner_factory(r'-\|/')
stars = scrolling_spinner_factory('*', 4, 1, hiding=False)
arrow = frame_spinner_factory('←↖↑↗→↘↓↙')
arrows = delayed_spinner_factory(arrow, 3, 1)
vertical = frame_spinner_factory('▁▂▃▄▅▆▇█▇▆▅▄▃▂')
waves = delayed_spinner_factory(vertical, 3, 2)
waves2 = delayed_spinner_factory(vertical, 3, 5)
waves3 = delayed_spinner_factory(vertical, 3, 7)
horizontal = frame_spinner_factory('▏▎▍▌▋▊▉█▉▊▋▌▍▎▏')
dots = frame_spinner_factory('⠁⠈⠐⠠⢀⡀⠄⠂')
dots_reverse = frame_spinner_factory('⣾⣷⣯⣟⡿⢿⣻⣽')
dots_waves = delayed_spinner_factory(dots, 5, 1)
dots_waves2 = delayed_spinner_factory(dots, 5, 2)
ball_scrolling = scrolling_spinner_factory('●', 3, 0, blank='∙')
balls_scrolling = scrolling_spinner_factory('●', 3, 1, blank='∙')
ball_bouncing = bouncing_spinner_factory('●', 8, 0, hiding=False)
balls_bouncing = bouncing_spinner_factory('●', 8, 1, hiding=False)
dots_recur = bouncing_spinner_factory('.', 3, 3)
bar_recur = bouncing_spinner_factory('=', 4, 3)
pointer = scrolling_spinner_factory('►', 5, 2, hiding=False)
arrows_recur = bouncing_spinner_factory('→', 6, 3, '←')
triangles = bouncing_spinner_factory('▶', 6, 2, '◀', hiding=False)
_triangles = bouncing_spinner_factory('▶▷', 6, 3, '◁◀')
triangles2 = delayed_spinner_factory(_triangles, 2, 9)
brackets = bouncing_spinner_factory('>', 8, 3, '<', hiding=False)
balls_filling = bouncing_spinner_factory('∙●', 10, 5, left_chars='○', hiding=False)
notes = bouncing_spinner_factory('♩♪', 10, 4, left_chars='♫♬')
notes2 = bouncing_spinner_factory('♩♪', 10, 4, left_chars='♫♬', hiding=False)
notes_scrolling = scrolling_spinner_factory('♩♪♫♬', 10, 4, hiding=False)
_arrows_left = scrolling_spinner_factory('<.', 6, 4, right=False)
_arrows_right = scrolling_spinner_factory('>.', 6, 4, right=True)
arrows_incoming = compound_spinner_factory(_arrows_right, _arrows_left)
arrows_outgoing = compound_spinner_factory(_arrows_left, _arrows_right)
real_arrow = scrolling_spinner_factory('>>------>', 18)
fish = scrolling_spinner_factory("><(((('>", 15, hiding=False)
fish2 = scrolling_spinner_factory('¸.·´¯`·.·´¯`·.¸¸.·´¯`·.¸><(((º>', 16)
fish_bouncing = bouncing_spinner_factory("><(((('>", 18, left_chars="<'))))><", hiding=False)
fishes = bouncing_spinner_factory('><>     ><>', 18, left_chars='<><  <><    <><')
message_scrolling = scrolling_spinner_factory('please wait...', right=False)
message_bouncing = bouncing_spinner_factory('please', 15, left_chars='wait', hiding=False)
long_message = bouncing_spinner_factory('processing', 15, left_chars='well, this is taking longer than anticipated, hold on')
pulse = frame_spinner_factory(
    r'•–––––––––––––',
    r'–•––––––––––––',
    r'––•–––––––––––',
    r'–––•––––––––––',
    r'––––•–––––––––',
    r'–––––√––––––––',
    r'–––––√\–––––––',
    r'–––––√\/––––––',
    r'–––––√\/•–––––',
    r'–––––√\/–•––––',
    r'––––––\/––•–––',
    r'–––––––/–––•––',
    r'––––––––––––•–',
    r'–––––––––––––•',
)
'''

