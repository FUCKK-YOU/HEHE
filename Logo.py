#£!Colour Code
rl1 = '\x1b[38;5;210m'
rl2 = '\x1b[38;5;89m'
gl1 = '\x1b[38;5;84m'
gl2 = '\x1b[38;5;119m'
gl3= '\x1b[38;5;118m'
gl4 = '\x1b[38;5;84m'
gl5 = '\x1b[38;5;82m'
gl6 = '\x1b[38;5;46m'
rl3= '\x1b[38;5;124m'
gx= '\x1b[38;5;46m'
red = '\x1b[38;5;160m'
green = '\x1b[38;5;46m'
purple = '\x1b[38;5;129m'
yellow  = '\x1b[38;5;226m'
mm = '\x1b[38;5;50m'
xd= '\x1b[38;5;29m'
white = '\x1b[38;5;15m'
my_color = [white,rl1,rl2,rl3,red,green,purple];warna = random.choice(my_color);loop,oks,cps,pcp,id = 0,[],[],[],[]

#£! logo

def logo():
    os.system('clear')
    print(f"""   
{xd}█████████████████████████████████████████████████
{xd}██{red}►{gl1}   d8888  d88888b d88888b  .d8b.  d888888b {red}◄{xd}██
{xd}██{red}►{gl4}  88   YP 88      88      d8   8b    88    {red}◄{xd}██
{xd}██{red}►{gl2}   8bo.   88ooooo 88ooo   88ooo88    88    {red}◄{xd}██
{xd}██{red}►{gl3}     Y8b  88      88      88   88    88    {red}◄{xd}██
{xd}██{red}►{gl5}  db   8D 88      88      88   88    88    {red}◄{xd}██
{xd}██{red}►{gl6}   8888Y  Y88888P YP      YP   YP    YP    {red}◄{xd}██
{xd}█████████████████████████████████████████████████
{xd}██{red}► {white}Fb {red}- {white}Sefat Sarker  {red}►{green}|{red}◄ {white}Github {red}- {white}SEFAT-777 {red}◄{xd}██
{xd}█████████████████████████████████████████████████""") 
def linex():
        print(f"{xd}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
