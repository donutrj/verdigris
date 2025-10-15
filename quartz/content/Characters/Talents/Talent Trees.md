# Alchemical
``` mermaid
graph LR

A["[[Talent List#Additives|Additives]]"]
B["[[Talent List#Alchemy|Alchemy]]"]
C["[[Talent List#All but the Dregs|All but the Dregs]]"]
D["[[Talent List#Batch Processing|Batch Processing]]"]
E["[[Talent List#Bare Essentials|Bare Essentials]]"]
F["[[Talent List#Lead to Gold|Lead to Gold]]"]
G["[[Talent List#Potion Belt|Potion Belt]]"]
H["[[Talent List#The Curwen Cycle|The Curwen Cycle]]"]

B --> D
D --> A
A --> C
G --> E
H --> F
A --> H
C --> F
D --> G

```
# Ancient Warfare
``` mermaid
graph LR

A["[[Talent List#Hardy|Hardy]]"]
B["[[Talent List#Strike Mighty Blow|Strike Mighty Blow]]"]
C["[[Talent List#Strong Back|Strong Back]]"]
D["[[Talent List#Berserk Charge|Berserk Charge]]"]
E["[[Talent List#Slayer|Slayer]]"]
F["[[Talent List#Iron Will|Iron Will]]"]
G["[[Talent List#Heavy Hand|Heavy Hand]]"]
H["[[Talent List#Flesh and Bone|Flesh and Bone]]"]
J["[[Talent List#Relentless|Relentless]]"]
K["[[Talent List#Back to the Wall|Back to the Wall]]"]
L["[[Talent List#Dazing Throw|Dazing Throw]]"]
M["[[Talent List#Random Bullshit Go|Random Bullshit Go]]"]
N["[[Talent List#Frenzy|Frenzy]]"]
O["[[Talent List#Unshakable|Unshakable]]"]
P["[[Talent List#Never Outmatched|Never Outmatched]]"]

F --> J
A --> B
A --> C
B --> D
B --> E
C --> F
C --> G
F --> K
G --> L
G --> M
K --> O
L --> O
M --> O
E --> H
D --> J
J --> N
P --> O
E --> P

```
# Apothecary 
``` mermaid
graph LR

A["[[Talent List#Physician|Physician]]"]
B["[[Talent List#Diagnose|Diagnose]]"]
C["[[Talent List#Sterilize|Sterilize]]"]
D["[[Talent List#Aprons|Aprons]]"]
E["[[Talent List#Medical Mal-Practice|Medical Mal-Practice]]"]
F["[[Talent List#Reputable|Reputable]]"]
G["[[Talent List#Field Dressing|Field Dressing]]"]
H["[[Talent List#Disease Resistant|Disease Resistant]]"]
I["[[Talent List#Precise Cut|Precise Cut]]"]
J["[[Talent List#Prosthesis|Prosthesis]]"]
K["[[Talent List#Surgery|Surgery]]"]
L["[[Talent List#Triage Expert|Triage Expert]]"]
O["[[Talent List#Mad Doctor|Mad Doctor]]"]
P["[[Talent List#Medic Here!|Medic Here!]]"]
M["[[Talent List#Bone Doctor|Bone Doctor]]"]

A --> B
A --> C
A --> M
C --> H
C --> G
B --> D
B --> E
C --> F
E --> I
G --> K
D --> L
D --> J
F --> P
K --> O
L --> O
J --> O
B --> H
M --> G

```
# Crafting
``` mermaid
graph LR

A["[[Talent List#Engineering|Engineering]]"]
B["[[Talent List#Fletcher|Fletcher]]"]
C["[[Talent List#Gadgeteering|Gadgeteering]]"]
D["[[Talent List#Guerrilla Warfare|Guerrilla Warfare]]"]
E["[[Talent List#Guild Grade|Guild Grade]]"]
F["[[Talent List#Handy|Handy]]"]
G["[[Talent List#Not Paying for That|Not Paying for That]]"]
H["[[Talent List#Smithing|Smithing]]"]
I["[[Talent List#Trinketeering|Trinketeering]]"]
J["[[Talent List#Woodworking|Woodworking]]"]
K["[[Talent List#Under Siege|Under Siege]]"]
L["[[Talent List#Up in Arms|Up in Arms]]"]

F --> J
F --> H
F --> G
J --> B
H --> L
G --> I
B --> D
L --> K
L --> E
I --> C
C --> A
E --> A
K --> A



```
# Criminal
``` mermaid
graph LR

A["[[Talent List#Break & Enter|Break & Enter]]"]
B["[[Talent List#Briber|Briber]]"]
C["[[Talent List#Bystander|Bystander]]"]
D["[[Talent List#Cat-Tongued|Cat-Tongued]]"]
E["[[Talent List#Cheat|Cheat]]"]
F["[[Talent List#Dirty Fighting|Dirty Fighting]]"]
G["[[Talent List#Embezzle|Embezzle]]"]
H["[[Talent List#Fast Hands|Fast Hands]]"]
I["[[Talent List#Get it Done|Get it Done]]"]
J["[[Talent List#I Know a Guy|I Know a Guy]]"]
K["[[Talent List#Master of Disguise|Master of Disguise]]"]
L["[[Talent List#Nose for Trouble|Nose for Trouble]]"]
M["[[Talent List#Ringleader|Ringleader]]"]
O["[[Talent List#Schemer|Schemer]]"]

J --> E
J --> F
J --> B
J --> L
E --> D
B --> G
F --> A
L --> C
E --> G
K --> O
C --> O
G --> O
O --> I
M --> I
A --> M
D --> M
J --> H
H --> A
E --> K


```
# Devotion
``` mermaid
graph LR

A(Devotee)
B(Favored)
C(Holy Leech)
D(Holy Visions)
E(Impassioned Zeal)
F(Miracle)
G(Righteous Fury)
H(Second Sight)
I(Taste of the Profane)

A --> D
A --> B
A --> E
B --> H


```
# Modern Warfare
``` mermaid
graph LR

A["[[Talent List#Blackpowder|Blackpowder]]"]
B["[[Talent List#Caracole|Caracole]]"]
C["[[Talent List#Commanding Presence|Commanding Presence]]"]
D["[[Talent List#Coolheaded|Coolheaded]]"]
E["[[Talent List#Deadeye Shot|Deadeye Shot]]"]
F["[[Talent List#Grizzled|Grizzled]]"]
G["[[Talent List#Light on Your Feet|Light on Your Feet]]"]
H["[[Talent List#Modern Techniques|Modern Techniques]]"]
I["[[Talent List#Pike Push|Pike Push]]"]
J["[[Talent List#Practiced Gunner|Practiced Gunner]]"]
K["[[Talent List#Professional|Professional]]"]
L["[[Talent List#Ready, Loose!|Ready, Loose!]]"]
M["[[Talent List#Sharpshooter|Sharpshooter]]"]
N["[[Talent List#Sniper|Sniper]]"]
O["[[Talent List#Sure Shot|Sure Shot]]"]

H --> K
H --> M
K --> D
K --> C
C --> B
C --> G
D --> I
G --> F
I --> F
M --> A
M --> L
A --> J
L --> N
L --> O
J --> E
N --> E
O --> E

```
# Orthodox Warfare
``` mermaid
graph LR

A["[[Talent List#Accurate Shot|Accurate Shot]]"]
B["[[Talent List#Combat Reflexes|Combat Reflexes]]"]
C["[[Talent List#Drilled|Drilled]]"]
D["[[Talent List#Flee!|Flee!]]"]
E["[[Talent List#Heroic|Heroic]]"]
F["[[Talent List#Ironclad|Ironclad]]"]
G["[[Talent List#Juggernaut|Juggernaut]]"]
H["[[Talent List#Saddleshot|Saddleshot]]"]
I["[[Talent List#Shieldmaster|Shieldmaster]]"]
J["[[Talent List#Strike to Injure|Strike to Injure]]"]
K["[[Talent List#Orthodox Techniques|Orthodox Techniques]]"]
L["[[Talent List#Tenacious|Tenacious]]"]
M["[[Talent List#Unsullied|Unsullied]]"]
N["[[Talent List#Veteran Status|Veteran Status]]"]
O["[[Talent List#Quickdraw|Quickdraw]]"]

K --> C
K --> B
C --> I
C --> J
B --> J
B --> D
B --> M
I --> F
I --> G
J --> L
L --> N
G --> N
M --> A
A --> O
M --> E
```
# Wizardry
``` mermaid
graph LR

A["[[Talent List#Blood Magic|Blood Magic]]"]
B["[[Talent List#Desperate Gambit|Desperate Gambit]]"]
C["[[Talent List#Dissipation|Dissipation]]"]
D["[[Talent List#Educated|Educated]]"]
E["[[Talent List#Enchantment|Enchantment]]"]
F["[[Talent List#Fine Penmanship|Fine Penmanship]]"]
G["[[Talent List#Gradient Synchronization|Gradient Synchronization]]"]
H["[[Talent List#Horseback Arcana|Horseback Arcana]]"]
I["[[Talent List#Magical Resistance|Magical Resistance]]"]
J["[[Talent List#Magician Saunter|Magician Saunter]]"]
K["[[Talent List#Spellwrite|Spellwrite]]"]
L["[[Talent List#Thaumic Attunement|Thaumic Attunement]]"]
M["[[Talent List#Thaumic Sensitivity|Thaumic Sensitivity]]"]
N["[[Talent List#War Wizard|War Wizard]]"]
O["[[Talent List#Studious|Studious]]"]

I --> N
D --> H
D --> M
D --> O
H --> J
M --> L
M --> I
O --> C
O --> F
J --> N
L --> B
I --> A
C --> G
N --> E
B --> E
A --> E
A --> K
G --> K

```