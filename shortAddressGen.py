"""
Lisk Short Address Generator.

Non-Standard Libary modules:
bitarray
nacl

"""
import os
import hashlib
import nacl.bindings
from bitarray import bitarray

wordlist = ['abandon', 'ability', 'able', 'about', 'above', 'absent', 'absorb',
            'abstract', 'absurd', 'abuse', 'access', 'accident', 'account',
            'accuse', 'achieve', 'acid', 'acoustic', 'acquire', 'across',
            'act', 'action', 'actor', 'actress', 'actual', 'adapt', 'add',
            'addict', 'address', 'adjust', 'admit', 'adult', 'advance',
            'advice', 'aerobic', 'affair', 'afford', 'afraid', 'again', 'age',
            'agent', 'agree', 'ahead', 'aim', 'air', 'airport', 'aisle',
            'alarm', 'album', 'alcohol', 'alert', 'alien', 'all', 'alley',
            'allow', 'almost', 'alone', 'alpha', 'already', 'also', 'alter',
            'always', 'amateur', 'amazing', 'among', 'amount', 'amused',
            'analyst', 'anchor', 'ancient', 'anger', 'angle', 'angry',
            'animal', 'ankle', 'announce', 'annual', 'another', 'answer',
            'antenna', 'antique', 'anxiety', 'any', 'apart', 'apology',
            'appear', 'apple', 'approve', 'april', 'arch', 'arctic', 'area',
            'arena', 'argue', 'arm', 'armed', 'armor', 'army', 'around',
            'arrange', 'arrest', 'arrive', 'arrow', 'art', 'artefact',
            'artist', 'artwork', 'ask', 'aspect', 'assault', 'asset', 'assist',
            'assume', 'asthma', 'athlete', 'atom', 'attack', 'attend',
            'attitude', 'attract', 'auction', 'audit', 'august', 'aunt',
            'author', 'auto', 'autumn', 'average', 'avocado', 'avoid', 'awake',
            'aware', 'away', 'awesome', 'awful', 'awkward', 'axis', 'baby',
            'bachelor', 'bacon', 'badge', 'bag', 'balance', 'balcony', 'ball',
            'bamboo', 'banana', 'banner', 'bar', 'barely', 'bargain', 'barrel',
            'base', 'basic', 'basket', 'battle', 'beach', 'bean', 'beauty',
            'because', 'become', 'beef', 'before', 'begin', 'behave', 'behind',
            'believe', 'below', 'belt', 'bench', 'benefit', 'best', 'betray',
            'better', 'between', 'beyond', 'bicycle', 'bid', 'bike', 'bind',
            'biology', 'bird', 'birth', 'bitter', 'black', 'blade', 'blame',
            'blanket', 'blast', 'bleak', 'bless', 'blind', 'blood', 'blossom',
            'blouse', 'blue', 'blur', 'blush', 'board', 'boat', 'body', 'boil',
            'bomb', 'bone', 'bonus', 'book', 'boost', 'border', 'boring',
            'borrow', 'boss', 'bottom', 'bounce', 'box', 'boy', 'bracket',
            'brain', 'brand', 'brass', 'brave', 'bread', 'breeze', 'brick',
            'bridge', 'brief', 'bright', 'bring', 'brisk', 'broccoli',
            'broken', 'bronze', 'broom', 'brother', 'brown', 'brush', 'bubble',
            'buddy', 'budget', 'buffalo', 'build', 'bulb', 'bulk', 'bullet',
            'bundle', 'bunker', 'burden', 'burger', 'burst', 'bus', 'business',
            'busy', 'butter', 'buyer', 'buzz', 'cabbage', 'cabin', 'cable',
            'cactus', 'cage', 'cake', 'call', 'calm', 'camera', 'camp', 'can',
            'canal', 'cancel', 'candy', 'cannon', 'canoe', 'canvas', 'canyon',
            'capable', 'capital', 'captain', 'car', 'carbon', 'card', 'cargo',
            'carpet', 'carry', 'cart', 'case', 'cash', 'casino', 'castle',
            'casual', 'cat', 'catalog', 'catch', 'category', 'cattle',
            'caught', 'cause', 'caution', 'cave', 'ceiling', 'celery',
            'cement', 'census', 'century', 'cereal', 'certain', 'chair',
            'chalk', 'champion', 'change', 'chaos', 'chapter', 'charge',
            'chase', 'chat', 'cheap', 'check', 'cheese', 'chef', 'cherry',
            'chest', 'chicken', 'chief', 'child', 'chimney', 'choice',
            'choose', 'chronic', 'chuckle', 'chunk', 'churn', 'cigar',
            'cinnamon', 'circle', 'citizen', 'city', 'civil', 'claim', 'clap',
            'clarify', 'claw', 'clay', 'clean', 'clerk', 'clever', 'click',
            'client', 'cliff', 'climb', 'clinic', 'clip', 'clock', 'clog',
            'close', 'cloth', 'cloud', 'clown', 'club', 'clump', 'cluster',
            'clutch', 'coach', 'coast', 'coconut', 'code', 'coffee', 'coil',
            'coin', 'collect', 'color', 'column', 'combine', 'come', 'comfort',
            'comic', 'common', 'company', 'concert', 'conduct', 'confirm',
            'congress', 'connect', 'consider', 'control', 'convince', 'cook',
            'cool', 'copper', 'copy', 'coral', 'core', 'corn', 'correct',
            'cost', 'cotton', 'couch', 'country', 'couple', 'course', 'cousin',
            'cover', 'coyote', 'crack', 'cradle', 'craft', 'cram', 'crane',
            'crash', 'crater', 'crawl', 'crazy', 'cream', 'credit', 'creek',
            'crew', 'cricket', 'crime', 'crisp', 'critic', 'crop', 'cross',
            'crouch', 'crowd', 'crucial', 'cruel', 'cruise', 'crumble',
            'crunch', 'crush', 'cry', 'crystal', 'cube', 'culture', 'cup',
            'cupboard', 'curious', 'current', 'curtain', 'curve', 'cushion',
            'custom', 'cute', 'cycle', 'dad', 'damage', 'damp', 'dance',
            'danger', 'daring', 'dash', 'daughter', 'dawn', 'day', 'deal',
            'debate', 'debris', 'decade', 'december', 'decide', 'decline',
            'decorate', 'decrease', 'deer', 'defense', 'define', 'defy',
            'degree', 'delay', 'deliver', 'demand', 'demise', 'denial',
            'dentist', 'deny', 'depart', 'depend', 'deposit', 'depth',
            'deputy', 'derive', 'describe', 'desert', 'design', 'desk',
            'despair', 'destroy', 'detail', 'detect', 'develop', 'device',
            'devote', 'diagram', 'dial', 'diamond', 'diary', 'dice', 'diesel',
            'diet', 'differ', 'digital', 'dignity', 'dilemma', 'dinner',
            'dinosaur', 'direct', 'dirt', 'disagree', 'discover', 'disease',
            'dish', 'dismiss', 'disorder', 'display', 'distance', 'divert',
            'divide', 'divorce', 'dizzy', 'doctor', 'document', 'dog', 'doll',
            'dolphin', 'domain', 'donate', 'donkey', 'donor', 'door', 'dose',
            'double', 'dove', 'draft', 'dragon', 'drama', 'drastic', 'draw',
            'dream', 'dress', 'drift', 'drill', 'drink', 'drip', 'drive',
            'drop', 'drum', 'dry', 'duck', 'dumb', 'dune', 'during', 'dust',
            'dutch', 'duty', 'dwarf', 'dynamic', 'eager', 'eagle', 'early',
            'earn', 'earth', 'easily', 'east', 'easy', 'echo', 'ecology',
            'economy', 'edge', 'edit', 'educate', 'effort', 'egg', 'eight',
            'either', 'elbow', 'elder', 'electric', 'elegant', 'element',
            'elephant', 'elevator', 'elite', 'else', 'embark', 'embody',
            'embrace', 'emerge', 'emotion', 'employ', 'empower', 'empty',
            'enable', 'enact', 'end', 'endless', 'endorse', 'enemy', 'energy',
            'enforce', 'engage', 'engine', 'enhance', 'enjoy', 'enlist',
            'enough', 'enrich', 'enroll', 'ensure', 'enter', 'entire', 'entry',
            'envelope', 'episode', 'equal', 'equip', 'era', 'erase', 'erode',
            'erosion', 'error', 'erupt', 'escape', 'essay', 'essence',
            'estate', 'eternal', 'ethics', 'evidence', 'evil', 'evoke',
            'evolve', 'exact', 'example', 'excess', 'exchange', 'excite',
            'exclude', 'excuse', 'execute', 'exercise', 'exhaust', 'exhibit',
            'exile', 'exist', 'exit', 'exotic', 'expand', 'expect', 'expire',
            'explain', 'expose', 'express', 'extend', 'extra', 'eye',
            'eyebrow', 'fabric', 'face', 'faculty', 'fade', 'faint', 'faith',
            'fall', 'false', 'fame', 'family', 'famous', 'fan', 'fancy',
            'fantasy', 'farm', 'fashion', 'fat', 'fatal', 'father', 'fatigue',
            'fault', 'favorite', 'feature', 'february', 'federal', 'fee',
            'feed', 'feel', 'female', 'fence', 'festival', 'fetch', 'fever',
            'few', 'fiber', 'fiction', 'field', 'figure', 'file', 'film',
            'filter', 'final', 'find', 'fine', 'finger', 'finish', 'fire',
            'firm', 'first', 'fiscal', 'fish', 'fit', 'fitness', 'fix', 'flag',
            'flame', 'flash', 'flat', 'flavor', 'flee', 'flight', 'flip',
            'float', 'flock', 'floor', 'flower', 'fluid', 'flush', 'fly',
            'foam', 'focus', 'fog', 'foil', 'fold', 'follow', 'food', 'foot',
            'force', 'forest', 'forget', 'fork', 'fortune', 'forum', 'forward',
            'fossil', 'foster', 'found', 'fox', 'fragile', 'frame', 'frequent',
            'fresh', 'friend', 'fringe', 'frog', 'front', 'frost', 'frown',
            'frozen', 'fruit', 'fuel', 'fun', 'funny', 'furnace', 'fury',
            'future', 'gadget', 'gain', 'galaxy', 'gallery', 'game', 'gap',
            'garage', 'garbage', 'garden', 'garlic', 'garment', 'gas', 'gasp',
            'gate', 'gather', 'gauge', 'gaze', 'general', 'genius', 'genre',
            'gentle', 'genuine', 'gesture', 'ghost', 'giant', 'gift', 'giggle',
            'ginger', 'giraffe', 'girl', 'give', 'glad', 'glance', 'glare',
            'glass', 'glide', 'glimpse', 'globe', 'gloom', 'glory', 'glove',
            'glow', 'glue', 'goat', 'goddess', 'gold', 'good', 'goose',
            'gorilla', 'gospel', 'gossip', 'govern', 'gown', 'grab', 'grace',
            'grain', 'grant', 'grape', 'grass', 'gravity', 'great', 'green',
            'grid', 'grief', 'grit', 'grocery', 'group', 'grow', 'grunt',
            'guard', 'guess', 'guide', 'guilt', 'guitar', 'gun', 'gym',
            'habit', 'hair', 'half', 'hammer', 'hamster', 'hand', 'happy',
            'harbor', 'hard', 'harsh', 'harvest', 'hat', 'have', 'hawk',
            'hazard', 'head', 'health', 'heart', 'heavy', 'hedgehog', 'height',
            'hello', 'helmet', 'help', 'hen', 'hero', 'hidden', 'high', 'hill',
            'hint', 'hip', 'hire', 'history', 'hobby', 'hockey', 'hold',
            'hole', 'holiday', 'hollow', 'home', 'honey', 'hood', 'hope',
            'horn', 'horror', 'horse', 'hospital', 'host', 'hotel', 'hour',
            'hover', 'hub', 'huge', 'human', 'humble', 'humor', 'hundred',
            'hungry', 'hunt', 'hurdle', 'hurry', 'hurt', 'husband', 'hybrid',
            'ice', 'icon', 'idea', 'identify', 'idle', 'ignore', 'ill',
            'illegal', 'illness', 'image', 'imitate', 'immense', 'immune',
            'impact', 'impose', 'improve', 'impulse', 'inch', 'include',
            'income', 'increase', 'index', 'indicate', 'indoor', 'industry',
            'infant', 'inflict', 'inform', 'inhale', 'inherit', 'initial',
            'inject', 'injury', 'inmate', 'inner', 'innocent', 'input',
            'inquiry', 'insane', 'insect', 'inside', 'inspire', 'install',
            'intact', 'interest', 'into', 'invest', 'invite', 'involve',
            'iron', 'island', 'isolate', 'issue', 'item', 'ivory', 'jacket',
            'jaguar', 'jar', 'jazz', 'jealous', 'jeans', 'jelly', 'jewel',
            'job', 'join', 'joke', 'journey', 'joy', 'judge', 'juice', 'jump',
            'jungle', 'junior', 'junk', 'just', 'kangaroo', 'keen', 'keep',
            'ketchup', 'key', 'kick', 'kid', 'kidney', 'kind', 'kingdom',
            'kiss', 'kit', 'kitchen', 'kite', 'kitten', 'kiwi', 'knee',
            'knife', 'knock', 'know', 'lab', 'label', 'labor', 'ladder',
            'lady', 'lake', 'lamp', 'language', 'laptop', 'large', 'later',
            'latin', 'laugh', 'laundry', 'lava', 'law', 'lawn', 'lawsuit',
            'layer', 'lazy', 'leader', 'leaf', 'learn', 'leave', 'lecture',
            'left', 'leg', 'legal', 'legend', 'leisure', 'lemon', 'lend',
            'length', 'lens', 'leopard', 'lesson', 'letter', 'level', 'liar',
            'liberty', 'library', 'license', 'life', 'lift', 'light', 'like',
            'limb', 'limit', 'link', 'lion', 'liquid', 'list', 'little',
            'live', 'lizard', 'load', 'loan', 'lobster', 'local', 'lock',
            'logic', 'lonely', 'long', 'loop', 'lottery', 'loud', 'lounge',
            'love', 'loyal', 'lucky', 'luggage', 'lumber', 'lunar', 'lunch',
            'luxury', 'lyrics', 'machine', 'mad', 'magic', 'magnet', 'maid',
            'mail', 'main', 'major', 'make', 'mammal', 'man', 'manage',
            'mandate', 'mango', 'mansion', 'manual', 'maple', 'marble',
            'march', 'margin', 'marine', 'market', 'marriage', 'mask', 'mass',
            'master', 'match', 'material', 'math', 'matrix', 'matter',
            'maximum', 'maze', 'meadow', 'mean', 'measure', 'meat', 'mechanic',
            'medal', 'media', 'melody', 'melt', 'member', 'memory', 'mention',
            'menu', 'mercy', 'merge', 'merit', 'merry', 'mesh', 'message',
            'metal', 'method', 'middle', 'midnight', 'milk', 'million',
            'mimic', 'mind', 'minimum', 'minor', 'minute', 'miracle', 'mirror',
            'misery', 'miss', 'mistake', 'mix', 'mixed', 'mixture', 'mobile',
            'model', 'modify', 'mom', 'moment', 'monitor', 'monkey', 'monster',
            'month', 'moon', 'moral', 'more', 'morning', 'mosquito', 'mother',
            'motion', 'motor', 'mountain', 'mouse', 'move', 'movie', 'much',
            'muffin', 'mule', 'multiply', 'muscle', 'museum', 'mushroom',
            'music', 'must', 'mutual', 'myself', 'mystery', 'myth', 'naive',
            'name', 'napkin', 'narrow', 'nasty', 'nation', 'nature', 'near',
            'neck', 'need', 'negative', 'neglect', 'neither', 'nephew',
            'nerve', 'nest', 'net', 'network', 'neutral', 'never', 'news',
            'next', 'nice', 'night', 'noble', 'noise', 'nominee', 'noodle',
            'normal', 'north', 'nose', 'notable', 'note', 'nothing', 'notice',
            'novel', 'now', 'nuclear', 'number', 'nurse', 'nut', 'oak', 'obey',
            'object', 'oblige', 'obscure', 'observe', 'obtain', 'obvious',
            'occur', 'ocean', 'october', 'odor', 'off', 'offer', 'office',
            'often', 'oil', 'okay', 'old', 'olive', 'olympic', 'omit', 'once',
            'one', 'onion', 'online', 'only', 'open', 'opera', 'opinion',
            'oppose', 'option', 'orange', 'orbit', 'orchard', 'order',
            'ordinary', 'organ', 'orient', 'original', 'orphan', 'ostrich',
            'other', 'outdoor', 'outer', 'output', 'outside', 'oval', 'oven',
            'over', 'own', 'owner', 'oxygen', 'oyster', 'ozone', 'pact',
            'paddle', 'page', 'pair', 'palace', 'palm', 'panda', 'panel',
            'panic', 'panther', 'paper', 'parade', 'parent', 'park', 'parrot',
            'party', 'pass', 'patch', 'path', 'patient', 'patrol', 'pattern',
            'pause', 'pave', 'payment', 'peace', 'peanut', 'pear', 'peasant',
            'pelican', 'pen', 'penalty', 'pencil', 'people', 'pepper',
            'perfect', 'permit', 'person', 'pet', 'phone', 'photo', 'phrase',
            'physical', 'piano', 'picnic', 'picture', 'piece', 'pig', 'pigeon',
            'pill', 'pilot', 'pink', 'pioneer', 'pipe', 'pistol', 'pitch',
            'pizza', 'place', 'planet', 'plastic', 'plate', 'play', 'please',
            'pledge', 'pluck', 'plug', 'plunge', 'poem', 'poet', 'point',
            'polar', 'pole', 'police', 'pond', 'pony', 'pool', 'popular',
            'portion', 'position', 'possible', 'post', 'potato', 'pottery',
            'poverty', 'powder', 'power', 'practice', 'praise', 'predict',
            'prefer', 'prepare', 'present', 'pretty', 'prevent', 'price',
            'pride', 'primary', 'print', 'priority', 'prison', 'private',
            'prize', 'problem', 'process', 'produce', 'profit', 'program',
            'project', 'promote', 'proof', 'property', 'prosper', 'protect',
            'proud', 'provide', 'public', 'pudding', 'pull', 'pulp', 'pulse',
            'pumpkin', 'punch', 'pupil', 'puppy', 'purchase', 'purity',
            'purpose', 'purse', 'push', 'put', 'puzzle', 'pyramid', 'quality',
            'quantum', 'quarter', 'question', 'quick', 'quit', 'quiz', 'quote',
            'rabbit', 'raccoon', 'race', 'rack', 'radar', 'radio', 'rail',
            'rain', 'raise', 'rally', 'ramp', 'ranch', 'random', 'range',
            'rapid', 'rare', 'rate', 'rather', 'raven', 'raw', 'razor',
            'ready', 'real', 'reason', 'rebel', 'rebuild', 'recall', 'receive',
            'recipe', 'record', 'recycle', 'reduce', 'reflect', 'reform',
            'refuse', 'region', 'regret', 'regular', 'reject', 'relax',
            'release', 'relief', 'rely', 'remain', 'remember', 'remind',
            'remove', 'render', 'renew', 'rent', 'reopen', 'repair', 'repeat',
            'replace', 'report', 'require', 'rescue', 'resemble', 'resist',
            'resource', 'response', 'result', 'retire', 'retreat', 'return',
            'reunion', 'reveal', 'review', 'reward', 'rhythm', 'rib', 'ribbon',
            'rice', 'rich', 'ride', 'ridge', 'rifle', 'right', 'rigid', 'ring',
            'riot', 'ripple', 'risk', 'ritual', 'rival', 'river', 'road',
            'roast', 'robot', 'robust', 'rocket', 'romance', 'roof', 'rookie',
            'room', 'rose', 'rotate', 'rough', 'round', 'route', 'royal',
            'rubber', 'rude', 'rug', 'rule', 'run', 'runway', 'rural', 'sad',
            'saddle', 'sadness', 'safe', 'sail', 'salad', 'salmon', 'salon',
            'salt', 'salute', 'same', 'sample', 'sand', 'satisfy', 'satoshi',
            'sauce', 'sausage', 'save', 'say', 'scale', 'scan', 'scare',
            'scatter', 'scene', 'scheme', 'school', 'science', 'scissors',
            'scorpion', 'scout', 'scrap', 'screen', 'script', 'scrub', 'sea',
            'search', 'season', 'seat', 'second', 'secret', 'section',
            'security', 'seed', 'seek', 'segment', 'select', 'sell', 'seminar',
            'senior', 'sense', 'sentence', 'series', 'service', 'session',
            'settle', 'setup', 'seven', 'shadow', 'shaft', 'shallow', 'share',
            'shed', 'shell', 'sheriff', 'shield', 'shift', 'shine', 'ship',
            'shiver', 'shock', 'shoe', 'shoot', 'shop', 'short', 'shoulder',
            'shove', 'shrimp', 'shrug', 'shuffle', 'shy', 'sibling', 'sick',
            'side', 'siege', 'sight', 'sign', 'silent', 'silk', 'silly',
            'silver', 'similar', 'simple', 'since', 'sing', 'siren', 'sister',
            'situate', 'six', 'size', 'skate', 'sketch', 'ski', 'skill',
            'skin', 'skirt', 'skull', 'slab', 'slam', 'sleep', 'slender',
            'slice', 'slide', 'slight', 'slim', 'slogan', 'slot', 'slow',
            'slush', 'small', 'smart', 'smile', 'smoke', 'smooth', 'snack',
            'snake', 'snap', 'sniff', 'snow', 'soap', 'soccer', 'social',
            'sock', 'soda', 'soft', 'solar', 'soldier', 'solid', 'solution',
            'solve', 'someone', 'song', 'soon', 'sorry', 'sort', 'soul',
            'sound', 'soup', 'source', 'south', 'space', 'spare', 'spatial',
            'spawn', 'speak', 'special', 'speed', 'spell', 'spend', 'sphere',
            'spice', 'spider', 'spike', 'spin', 'spirit', 'split', 'spoil',
            'sponsor', 'spoon', 'sport', 'spot', 'spray', 'spread', 'spring',
            'spy', 'square', 'squeeze', 'squirrel', 'stable', 'stadium',
            'staff', 'stage', 'stairs', 'stamp', 'stand', 'start', 'state',
            'stay', 'steak', 'steel', 'stem', 'step', 'stereo', 'stick',
            'still', 'sting', 'stock', 'stomach', 'stone', 'stool', 'story',
            'stove', 'strategy', 'street', 'strike', 'strong', 'struggle',
            'student', 'stuff', 'stumble', 'style', 'subject', 'submit',
            'subway', 'success', 'such', 'sudden', 'suffer', 'sugar',
            'suggest', 'suit', 'summer', 'sun', 'sunny', 'sunset', 'super',
            'supply', 'supreme', 'sure', 'surface', 'surge', 'surprise',
            'surround', 'survey', 'suspect', 'sustain', 'swallow', 'swamp',
            'swap', 'swarm', 'swear', 'sweet', 'swift', 'swim', 'swing',
            'switch', 'sword', 'symbol', 'symptom', 'syrup', 'system', 'table',
            'tackle', 'tag', 'tail', 'talent', 'talk', 'tank', 'tape',
            'target', 'task', 'taste', 'tattoo', 'taxi', 'teach', 'team',
            'tell', 'ten', 'tenant', 'tennis', 'tent', 'term', 'test', 'text',
            'thank', 'that', 'theme', 'then', 'theory', 'there', 'they',
            'thing', 'this', 'thought', 'three', 'thrive', 'throw', 'thumb',
            'thunder', 'ticket', 'tide', 'tiger', 'tilt', 'timber', 'time',
            'tiny', 'tip', 'tired', 'tissue', 'title', 'toast', 'tobacco',
            'today', 'toddler', 'toe', 'together', 'toilet', 'token', 'tomato',
            'tomorrow', 'tone', 'tongue', 'tonight', 'tool', 'tooth', 'top',
            'topic', 'topple', 'torch', 'tornado', 'tortoise', 'toss', 'total',
            'tourist', 'toward', 'tower', 'town', 'toy', 'track', 'trade',
            'traffic', 'tragic', 'train', 'transfer', 'trap', 'trash',
            'travel', 'tray', 'treat', 'tree', 'trend', 'trial', 'tribe',
            'trick', 'trigger', 'trim', 'trip', 'trophy', 'trouble', 'truck',
            'true', 'truly', 'trumpet', 'trust', 'truth', 'try', 'tube',
            'tuition', 'tumble', 'tuna', 'tunnel', 'turkey', 'turn', 'turtle',
            'twelve', 'twenty', 'twice', 'twin', 'twist', 'two', 'type',
            'typical', 'ugly', 'umbrella', 'unable', 'unaware', 'uncle',
            'uncover', 'under', 'undo', 'unfair', 'unfold', 'unhappy',
            'uniform', 'unique', 'unit', 'universe', 'unknown', 'unlock',
            'until', 'unusual', 'unveil', 'update', 'upgrade', 'uphold',
            'upon', 'upper', 'upset', 'urban', 'urge', 'usage', 'use',
            'used', 'useful', 'useless', 'usual', 'utility', 'vacant',
            'vacuum', 'vague', 'valid', 'valley', 'valve', 'van', 'vanish',
            'vapor', 'various', 'vast', 'vault', 'vehicle', 'velvet', 'vendor',
            'venture', 'venue', 'verb', 'verify', 'version', 'very', 'vessel',
            'veteran', 'viable', 'vibrant', 'vicious', 'victory', 'video',
            'view', 'village', 'vintage', 'violin', 'virtual', 'virus', 'visa',
            'visit', 'visual', 'vital', 'vivid', 'vocal', 'voice', 'void',
            'volcano', 'volume', 'vote', 'voyage', 'wage', 'wagon', 'wait',
            'walk', 'wall', 'walnut', 'want', 'warfare', 'warm', 'warrior',
            'wash', 'wasp', 'waste', 'water', 'wave', 'way', 'wealth',
            'weapon', 'wear', 'weasel', 'weather', 'web', 'wedding', 'weekend',
            'weird', 'welcome', 'west', 'wet', 'whale', 'what', 'wheat',
            'wheel', 'when', 'where', 'whip', 'whisper', 'wide', 'width',
            'wife', 'wild', 'will', 'win', 'window', 'wine', 'wing', 'wink',
            'winner', 'winter', 'wire', 'wisdom', 'wise', 'wish', 'witness',
            'wolf', 'woman', 'wonder', 'wood', 'wool', 'word', 'work', 'world',
            'worry', 'worth', 'wrap', 'wreck', 'wrestle', 'wrist', 'write',
            'wrong', 'yard', 'year', 'yellow', 'you', 'young', 'youth',
            'zebra', 'zero', 'zone', 'zoo']


def main():
    """Find Short Lisk Addresses."""
    options = setup()

    maxLength = int(options.get('maxLength')) - 1
    bip39 = options.get('bip39')
    writePreference = options.get('writePreference')

    if bip39 is True:

        try:

            getBIP39Addresses(maxLength, writePreference)

        except KeyboardInterrupt:

            print()
            input('(Press any key to exit)')
            print()

    else:

        try:

            getPkAddresses(maxLength, writePreference)

        except KeyboardInterrupt:

            print()
            input('(Press any key to exit)')
            print()


def setup():
    """Display header and get user options."""
    header()

    options = getOptions()

    showChoices(options)

    return options


def header():
    """Print program header and instructions."""
    print('''
----------------------------------------------------------------
                   _   ___           __
                  / | / (_)___ ___  / /_  __  _______
                 /  |/ / / __ `__ \/ __ \/ / / / ___/
                / /|  / / / / / / / /_/ / /_/ (__  )
               /_/ |_/_/_/ /_/ /_/_.___/\__,_/____/

                   LISK SHORT ADDRESS GENERATOR
                      Please Vote for Nimbus
                 Donate to 12313256070705265970L

----------------------------------------------------------------
This program generates Lisk addresses.

The user may specify the following options:

    - Maximum Lisk Address Length to return.
    - Whether addresses must be BIP39-compliant.
      (Non-BIP39-compliant addresses are faster to generate and
      return a secret key rather than a BIP39 passphrase).
    - Whether to write results to file.

Note:  Addresses shorter than 16 characters become increasingly
       difficult to find.

Enter CTRL-C to Exit.
----------------------------------------------------------------
''')


def getOptions():
    """Get user options."""
    maxLength = getMaxLength()

    bip39 = getBIP39()

    writePreference = getWriteStatus()

    print()

    options = {"maxLength": maxLength, "bip39": bip39, 'writePreference':
               writePreference}

    return options


def showChoices(options):
    """Show user's selected options."""
    print('----------------------------------------------------------------')

    print(f"- Searching for Lisk Addresses that are" +
          f" {options.get('maxLength')} characters or less.")

    if options.get('bip39') is True:

        print("- Only BIP39-compliant addresses will be generated.")

    else:

        print("- Generated addresses will not be BIP39-compliant.")

    if options.get('writePreference') is True:

        print("- Results will be displayed and written to 'shortAddresses.txt'\
              .")

    else:

        print("- Results will not be written to file.")

    print()

    print("Enter CTRL-C to Exit.")

    print('----------------------------------------------------------------')

    print('...')

    print()


def getBIP39Addresses(maxLength, writePreference):
    """Generate BIP39-compliant Lisk Addresses."""
    while 1:

        passphrase = getBIP39Passphrase()

        pk = getPublicKeyFromPassphrase(passphrase)

        intLiskAddress = getAddressFromPublicKey(pk)

        if len(str(intLiskAddress)) <= maxLength:

            printBIP39Address(passphrase, intLiskAddress)

            if writePreference is True:

                writeBIP39Address(passphrase, intLiskAddress)


def getPkAddresses(maxLength, writePreference):
    """Generate non-BIP39-compliant Lisk Addresses."""
    keyPair = nacl.bindings.crypto_sign_keypair

    while 1:

        pk, sk = keyPair()

        intLiskAddress = getAddressFromPublicKey(pk)

        if len(str(intLiskAddress)) <= maxLength:

            printPkAddress(pk, sk, intLiskAddress)

        if writePreference is True:

            writePkAddress(pk, sk, intLiskAddress)


def getBIP39Passphrase():
    """Generate BIP39-compliant Passphrase."""
    entropy = os.urandom(16)

    checksum = hashlib.sha256(entropy).digest()

    entropyBits = bitarray()

    entropyBits.frombytes(entropy)

    checksumBits = bitarray()

    checksumBits.frombytes(checksum)

    entropyBits.extend(checksumBits)

    fullEntropy = entropyBits[0:132]

    wordIndexes = [int(fullEntropy[i:i+11].to01(), 2)
                   for i in range(0, len(fullEntropy), 11)]

    passphrase = ' '.join([wordlist[i] for i in wordIndexes])

    return passphrase


def getPublicKeyFromPassphrase(passphrase):
    """Generate Public Key from BIP39-compliant passphrase."""
    passphraseBytes = bytes(passphrase, 'utf-8')

    passphraseHash = hashlib.sha256(passphraseBytes).digest()

    pk, sk = nacl.bindings.crypto_sign_seed_keypair(passphraseHash)

    return pk


def getAddressFromPublicKey(publicKey):
    """Calculate Lisk Address from Public Key."""
    publicKeyHash = hashlib.sha256(publicKey).digest()

    pkBytes = bytearray(publicKeyHash[0:8])

    pkBytes.reverse()

    intLiskAddress = int.from_bytes(pkBytes, byteorder='big')

    return intLiskAddress


def getMaxLength():
    """Determine Length of Lisk Address."""
    again = True

    while again is True:

        maxLength = input("Enter maximum length of Lisk Address to find: ")

        if maxLength.isnumeric() is True and float(maxLength) > 0:

            again = False

    return maxLength


def getBIP39():
    """Ask user whether generated address should be BIP39-compliant."""
    again = True

    while again is True:

        bip39compliant = input("Should generated addresses be" +
                               " BIP39-compliant? (y/n): ")

        if bip39compliant.lower() == 'y' or bip39compliant.lower() == 'n':

            if bip39compliant.lower() == 'y':

                bip39 = True

            else:

                bip39 = False

            again = False

    return bip39


def getWriteStatus():
    """Ask user whether to write results to file."""
    again = True

    while again is True:

        writeToFile = input("Would you like to write results to a text file?" +
                            " (y/n): ")

        if writeToFile.lower() == 'y' or writeToFile.lower() == 'n':

            if writeToFile.lower() == 'y':

                writePreference = True

            else:

                writePreference = False

            again = False

    return writePreference


def printBIP39Address(passphrase, intLiskAddress):
    """Print BIP39-compliant Lisk Address, Passphrase, and Length."""
    liskAddress = str(intLiskAddress) + 'L'
    print('Lisk Address:\t' + liskAddress)
    print('Length:  ' + '\t' + str(len(liskAddress)))
    print('Passphrase:\t' + passphrase)
    print()


def writeBIP39Address(passphrase, intLiskAddress):
    """Write BIP39-compliant address, passphrase, length to file."""
    liskAddress = str(intLiskAddress) + 'L'
    outfile = open('shortAddresses.txt', 'a')
    outfile.write('Lisk Address:\t' + (str(intLiskAddress) + 'L\n'))
    outfile.write('Length:  ' + '\t' + str(len(liskAddress)) + '\n')
    outfile.write('Passphrase:\t' + passphrase + '\n')
    outfile.write(' ' + '\n')
    outfile.close()


def printPkAddress(pk, sk, intLiskAddress):
    """Display non-BIP39-compliant address, pk, sk & length."""
    liskAddress = str(intLiskAddress) + 'L'
    print('Lisk Address:\t' + liskAddress)
    print('Length:  ' + '\t' + str(len(liskAddress)))
    print('Public Key:\t' + pk.hex())
    print('Secret Key:\t' + sk.hex())
    print()


def writePkAddress(pk, sk, intLiskAddress):
    """Write non-BIP39-compliant address, pk, sk, & length to file."""
    liskAddress = str(intLiskAddress) + 'L'
    outfile = open('shortAddresses.txt', 'a')
    outfile.write('Lisk Address:\t' + (str(intLiskAddress) + 'L\n'))
    outfile.write('Length:  ' + '\t' + str(len(liskAddress)) + '\n')
    outfile.write('Public Key: ' + '\t' + pk.hex() + '\n')
    outfile.write('Secret Key: ' + '\t' + sk.hex() + '\n')
    outfile.write(' ' + '\n')


main()
