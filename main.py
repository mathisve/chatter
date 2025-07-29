import random
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True, convert=True, strip=False)

# --- Sample Data ---
locations = [
    "Sector 4-B", "Northern Ridge", "Observation Post 7", "Atmospheric Relay 2",
    "Docking Bay Alpha", "Thermal Vents", "Subsurface Caverns", "Control Room Delta",
    "Comms Tower Epsilon", "Glacial Drift Field", "Supply Depot Gamma",
    "Alien Ruins Zeta", "Deep Space Relay 9", "Crystal Caverns", "Nebula Outpost X",
    "Ion Storm Zone", "Quantum Research Lab", "Frozen Expanse", "Volcanic Ridge",
    "Magnetic Field Station", "Asteroid Mining Site",
    "Event Horizon Perimeter", "Singularity Research Annex", "Helium-3 Refinery",
    "Obsidian Plateau", "Bio-Dome 3", "Stellar Nursery Beta", "Dark Matter Observatory",
    "Hydroponics Lab", "Meteor Impact Site 12", "Graviton Field Array",
    "Ice Crust Borehole", "Gamma Ray Listening Post", "Plasma Conduit",
    "Wormhole Approach Vector", "Solar Array Theta", "Frozen Lake Atka",
    "Suborbital Platform 6", "Ancient Beacon Ruins", "Exobiology Habitat",
    "Xenobotanical Garden", "Terraforming Control Spire", "Blacksite Vault 17",
    "Aurora Passage", "Red Sand Expanse", "Lagrange Point L2 Outpost",
    "Temporal Rift Margin", "Magnetar Research Node"
]

entities = [
    "Probe-17", "Drone X3", "Supply Rover", "Outpost-6", "Sensor Array Sigma",
    "Research Pod Theta", "Beacon-12", "Mining Rig-4", "Orbiting Relay-5",
    "Defense Grid Node", "Terraforming Unit-3",
    "Crewman Jax", "Engineer Lira", "Commander Voss", "Medic Tali", "Pilot Ryn",
    "Navigator Sera", "Technician Dex", "AI Unit Zed", "Scout Drone 21", "Cargo Bot 8",
    "Starship Horizon", "Scout Ship Vela", "AI Core Athena", "Alien Entity Xalor",
    "Recon Drone 44", "Maintenance Bot 29", "Satellite Sigma-4", "Sentinel Drone 9",
    "Astro-Navigator Pex", "Alien Observer Qiln", "Cargo Shuttle Tycho", "Orbital Habitat Z3",
    "Researcher Mina", "Commander Halv", "Bio-Drone 12", "Satellite Orion",
    "Scout Vessel Prism", "Automaton Vega", "Alien Vessel Kyra", "AI Unit Omega",
    "Surveyor Drone 88", "Technician Varn", "Xenoform Lyris", "Explorer Ship Dauntless",
    "Security Bot 7", "Alien AI Virel", "Deep Space Probe 23", "Pilot Zhen",
    "Satellite Helios", "Outpost AI Nyx", "Alien Scientist T'karn", "Terraformer Drone 5"
]

events = [
    "magnetic anomaly detected", "low-frequency signal intercepted", "thermal spike",
    "seismic fluctuation", "atmospheric pressure drop", "unidentified object sighted",
    "power fluctuation", "data packet received", "relay misalignment",
    "oxygen levels nominal", "communications restored", "lifeform signature detected",
    "solar flare activity rising", "core temperature stabilizing", "subsurface movement detected",
    "radiation burst detected", "sensor calibration required", "navigation system reboot",
    "energy reserves low", "system integrity compromised",
    "graviton surge detected", "alien transmission decoded", "engine malfunction reported",
    "system reboot in progress", "quantum entanglement failure", "hull breach sealed",
    "unknown artifact recovered", "plasma storm approaching", "nanite swarm contained",
    "blackout event in progress", "wormhole instability detected", "biological contamination alert",
    "cryo-chamber malfunction", "AI logic fault", "navigation data corrupted",
    "asteroid collision averted", "hyperspace jump successful", "alien vessel approaching",
    "subspace interference detected", "emergency lockdown initiated", "crew distress signal sent",
    "energy spike in core", "data corruption event", "xenobotanical specimen found",
    "temporal distortion registered", "gravity wave anomaly", "satellite link lost",
    "solar panel array failure", "critical coolant leak", "bioscan anomaly",
    "meteor shower impact", "ionizing radiation surge", "communication relay offline"
]

channels = [
    "COM-LINK", "ASTRONET", "LOCAL-NET", "DEEP-FIELD", "SURFACE OPS", "SUBSPACE",
    "MISSION CTRL", "SCIENCE LAB", "ENGINEERING", "SECURITY", "MED BAY"
]

status = [
    "STANDBY", "ACTIVE", "OFFLINE", "DEGRADED", "CALIBRATING", "LINK LOST", "SYNCING", "OVERRIDE",
    "REBOOTING", "ERROR", "MAINTENANCE", "IDLE", "ENGAGED", "LOCKED", "UNSTABLE"
]

def generate_random_graph():
    titles = [
        "POWER OUTPUT", "RADIATION LEVELS", "TEMPERATURE", "OXYGEN LEVELS", "ENERGY CONSUMPTION", "SIGNAL STRENGTH",
        "SOLAR FLUX", "COSMIC RAY DENSITY", "GRAVITY WAVE DETECTIONS", "SIGNAL DELAY", "ASTEROID TRAJECTORY"
    ]
    units = {
        "POWER OUTPUT": "kW",
        "RADIATION LEVELS": "mSv",
        "TEMPERATURE": "°C",
        "OXYGEN LEVELS": "%",
        "ENERGY CONSUMPTION": "MW",
        "SIGNAL STRENGTH": "dB",
        "SOLAR FLUX": "W/m²",
        "COSMIC RAY DENSITY": "particles/cm³",
        "GRAVITY WAVE DETECTIONS": "events/hr",
        "SIGNAL DELAY": "ms",
        "ASTEROID TRAJECTORY": "km"
    }
    axis_labels_options = {
        "POWER OUTPUT": "time (s)",
        "RADIATION LEVELS": "time (min)",
        "TEMPERATURE": "time (min)",
        "OXYGEN LEVELS": "time (min)",
        "ENERGY CONSUMPTION": "time (s)",
        "SIGNAL STRENGTH": "time (s)",
        "SOLAR FLUX": random.choice(["time (s)", "time (min)", "time (hr)"]),
        "COSMIC RAY DENSITY": random.choice(["time (min)", "time (hr)", "time (day)"]),
        "GRAVITY WAVE DETECTIONS": random.choice(["time (hr)", "time (day)"]),
        "SIGNAL DELAY": random.choice(["distance (km)", "distance (AU)"]),
        "ASTEROID TRAJECTORY": random.choice(["distance (km)", "distance (AU)"])
    }
    title = random.choice(titles)
    unit = units[title]
    axis_label = axis_labels_options.get(title, "time (s)")
    length = random.randint(15, 25)
    values = []

    # Generate baseline values and smooth variations depending on the title
    if title == "SOLAR FLUX":
        baseline = random.uniform(1300, 1400)  # typical solar constant W/m²
        variation_range = 50
    elif title == "COSMIC RAY DENSITY":
        baseline = random.uniform(0.1, 1.0)
        variation_range = 0.3
    elif title == "GRAVITY WAVE DETECTIONS":
        baseline = random.uniform(0, 10)
        variation_range = 3
    elif title == "SIGNAL DELAY":
        baseline = random.uniform(100, 500)
        variation_range = 50
    elif title == "ASTEROID TRAJECTORY":
        baseline = random.uniform(10000, 50000)
        variation_range = 5000
    elif title == "RADIATION LEVELS":
        baseline = random.uniform(0.1, 5.0)
        variation_range = 2.0
    elif title == "TEMPERATURE":
        baseline = random.uniform(-80, 120)
        variation_range = 10
    elif title == "OXYGEN LEVELS":
        baseline = random.uniform(19, 23)
        variation_range = 2
    elif title == "ENERGY CONSUMPTION":
        baseline = random.uniform(50, 150)
        variation_range = 20
    elif title == "SIGNAL STRENGTH":
        baseline = random.uniform(10, 60)
        variation_range = 15
    elif title == "POWER OUTPUT":
        baseline = random.uniform(30, 70)
        variation_range = 20
    else:
        baseline = random.uniform(30, 70)
        variation_range = 20

    values.append(baseline)
    for _ in range(1, length):
        change = random.uniform(-variation_range/4, variation_range/4)
        new_val = values[-1] + change
        # Clamp values between 0 and max expected value
        if title in ["SOLAR FLUX"]:
            new_val = max(1200, min(1500, new_val))
        elif title in ["COSMIC RAY DENSITY"]:
            new_val = max(0, min(2, new_val))
        elif title in ["GRAVITY WAVE DETECTIONS"]:
            new_val = max(0, min(20, new_val))
        elif title in ["SIGNAL DELAY"]:
            new_val = max(50, min(600, new_val))
        elif title in ["ASTEROID TRAJECTORY"]:
            new_val = max(5000, min(60000, new_val))
        elif title in ["RADIATION LEVELS"]:
            new_val = max(0, min(10, new_val))
        elif title in ["TEMPERATURE"]:
            new_val = max(-100, min(150, new_val))
        elif title in ["OXYGEN LEVELS"]:
            new_val = max(15, min(25, new_val))
        elif title in ["ENERGY CONSUMPTION"]:
            new_val = max(20, min(200, new_val))
        elif title in ["SIGNAL STRENGTH"]:
            new_val = max(0, min(80, new_val))
        else:
            new_val = max(0, min(100, new_val))
        values.append(new_val)

    max_val = max(values)
    min_val = min(values)
    max_bar_length = 30  # max width of bar

    # Normalize values to bar length
    bars = [int((v - min_val) / (max_val - min_val) * max_bar_length) if max_val != min_val else max_bar_length // 2 for v in values]

    lines = []
    min_max_line = f"{Fore.GREEN + Style.BRIGHT}Min: {min_val:8.2f} {unit} {' ' * (max_bar_length - 10)}Max: {max_val:8.2f} {unit}"
    header = f"{Fore.GREEN + Style.BRIGHT}{title.center(max_bar_length + 20)}"
    lines.append(min_max_line)
    lines.append(header)
    axis_label_line = f"{Fore.GREEN + Style.BRIGHT}X-Axis: {axis_label}"
    lines.append(axis_label_line)
    # Vertical axis marker at left with connecting line
    for i, bar_len in enumerate(bars):
        bar = "#" * bar_len
        lines.append(f"{Fore.GREEN + Style.BRIGHT}{str(i+1).rjust(2)} |{bar.ljust(max_bar_length)}|")
    # Horizontal axis
    axis_numbers = "    "  # space for index numbers
    for i in range(1, length + 1):
        if i % 5 == 0 or i == 1 or i == length:
            axis_numbers += str(i).rjust(2)
        else:
            axis_numbers += "  "
    lines.append(f"{Fore.GREEN + Style.BRIGHT}    {'-' * (max_bar_length + 2)}")
    lines.append(f"{Fore.GREEN + Style.BRIGHT}{axis_numbers}")
    # Units label centered below axis
    unit_label = f"Unit: {unit}"
    lines.append(f"{Fore.GREEN + Style.BRIGHT}{unit_label.center(max_bar_length + 20)}")
    return lines

def generate_solar_system_map():
    # Helper to generate a random name (star/planet) from syllables and numbers
    def random_name(is_star=False):
        syllables = [
            "ka", "ze", "lo", "vi", "ra", "to", "xi", "mu", "sy", "pa", "qu", "ni", "ba", "lu", "ga", "re", "do", "fi"
        ]
        name = "".join(random.choice(syllables).capitalize() for _ in range(random.randint(2, 3)))
        if random.random() < 0.5:
            name += str(random.randint(1, 99))
        if is_star:
            # Star names sometimes have a Greek letter prefix or "HD" style
            prefixes = ["HD ", "Tau ", "Xi ", "Alpha ", "Beta ", "Gamma ", "Delta ", ""]
            name = random.choice(prefixes) + name
        return name

    # Number of planets (between 4 and 8)
    num_planets = random.randint(4, 8)
    # Star name
    star_name = random_name(is_star=True)
    # Planets: each with a name and symbol
    planets = []
    for i in range(num_planets):
        pname = random_name()
        symbol = "(O)" if i in [0, num_planets-1] or random.random() < 0.3 else "(o)"
        planets.append({"name": pname, "symbol": symbol})

    # Map formatting
    # We'll use vertical orbits with the star at the bottom center, planets above, and lines connecting
    # We'll align everything to a fixed width for cohesiveness
    width = 55
    sun_line = width // 2
    # Build lines from top (outermost planet) to bottom (star)
    map_lines = []
    orbit_spacing = 2  # vertical lines between orbits
    # Calculate the max name+symbol length for alignment
    max_p_len = max(len(p["name"] + " " + p["symbol"]) for p in planets)
    star_label = f"{star_name} (O)"
    star_label_pad = (width - len(star_label)) // 2

    # For each planet, print planet name/symbol centered, then a line down to next
    for idx, planet in enumerate(planets):
        planet_label = f"{planet['name']} {planet['symbol']}"
        pad = (width - len(planet_label)) // 2
        map_lines.append(" " * pad + Fore.GREEN + Style.BRIGHT + planet_label + Style.RESET_ALL)
        # Draw orbit line to next (unless last planet)
        if idx < num_planets - 1:
            # Draw a line: center-aligned, using "===" or "---"
            line_char = "===" if planet["symbol"] == "(O)" else "---"
            map_lines.extend([
                " " * (width // 2 - 1) + Fore.GREEN + Style.BRIGHT + "|" + Style.RESET_ALL,
                " " * (width // 2 - len(line_char)//2) + Fore.GREEN + Style.BRIGHT + line_char + Style.RESET_ALL,
                " " * (width // 2 - 1) + Fore.GREEN + Style.BRIGHT + "|" + Style.RESET_ALL,
            ])
    # Now, below planets, the star (centered)
    map_lines.append(" " * star_label_pad + Fore.GREEN + Style.BRIGHT + star_label + Style.RESET_ALL)
    # Optionally, a little sparkle below the star
    sparkle = " " * (width // 2 - 2) + Fore.GREEN + Style.BRIGHT + "*  *  *" + Style.RESET_ALL
    map_lines.append(sparkle)
    return map_lines

# --- Line generator ---

# --- Fictional Time State ---
# 400 soluses per year, 8 marks per year, 36 soluses per mark
# 36 hours per solus, 60 minutes, 60 seconds

# Global variables for current fictional time
_fictional_year = None
_fictional_mark = None
_fictional_solus = None
_fictional_hour = None
_fictional_minute = None
_fictional_second = None

def _init_fictional_time():
    global _fictional_year, _fictional_mark, _fictional_solus, _fictional_hour, _fictional_minute, _fictional_second
    _fictional_year = random.randint(1, 999)
    _fictional_mark = random.randint(1, 8)
    _fictional_solus = random.randint(1, 36)
    _fictional_hour = random.randint(0, 35)
    _fictional_minute = random.randint(0, 59)
    _fictional_second = random.randint(0, 59)

_init_fictional_time()

def generate_fictional_timestamp():
    """
    Advances global fictional time by one second and returns formatted timestamp.
    Rolls over seconds, minutes, hours, soluses, marks, and years according to the fictional calendar.
    """
    global _fictional_year, _fictional_mark, _fictional_solus, _fictional_hour, _fictional_minute, _fictional_second
    # Advance one second
    _fictional_second += 1
    if _fictional_second >= 60:
        _fictional_second = 0
        _fictional_minute += 1
        if _fictional_minute >= 60:
            _fictional_minute = 0
            _fictional_hour += 1
            if _fictional_hour >= 36:
                _fictional_hour = 0
                _fictional_solus += 1
                if _fictional_solus > 36:
                    _fictional_solus = 1
                    _fictional_mark += 1
                    if _fictional_mark > 8:
                        _fictional_mark = 1
                        _fictional_year += 1
                        if _fictional_year > 999:
                            _fictional_year = 1
    # Format: YR-### MK-# SL-## HH:MM:SS
    return f"YR-{_fictional_year:03d} MK-{_fictional_mark} SL-{_fictional_solus:02d} {_fictional_hour:02d}:{_fictional_minute:02d}:{_fictional_second:02d}"

def fake_terminal_line():
    t = generate_fictional_timestamp()
    source = random.choice(entities)
    location = random.choice(locations)
    channel = random.choice(channels)
    evt = random.choice(events)
    st = random.choice(status)

    # Encryption-related messages
    encryption_events = [
        "ENCRYPTION KEY ROTATION", "NEW SIGNATURE GENERATED", "DECRYPTION ATTEMPT SUCCESSFUL",
        "DECRYPTION ATTEMPT FAILED", "ENCRYPTION PROTOCOL UPDATED", "SECURE CHANNEL ESTABLISHED",
        "AUTHENTICATION TOKEN EXPIRED", "SECURITY HANDSHAKE INITIATED", "DATA ENCRYPTED",
        "DATA DECRYPTED", "ENCRYPTION MODULE RESTARTED"
    ]

    # Color selection
    # Mostly green, with small chance of yellow or cyan for variety
    color_choice = random.random()
    if color_choice < 0.85:
        color = Fore.GREEN
    elif color_choice < 0.925:
        color = Fore.YELLOW
    else:
        color = Fore.CYAN
    color = color + Style.BRIGHT

    critical_color = Fore.RED + Style.BRIGHT

    crew_chat_msgs = [
        "Coffee machine offline again.", "Anyone seen the rover?", "Stars look brighter tonight.",
        "Lost the calibration data.", "System reboot scheduled at 0300.", "Alien artifact found nearby.",
        "Rover stuck in the mud.", "Signal strength dropping fast.", "Emergency drill in 10 minutes.",
        "New shipment of supplies arrived.", "Strange noises from the vents.", "Crew morale is high.",
        "Power fluctuations in sector 9.", "Sensor array needs cleaning.", "Data backlog increasing.",
        "Holo-deck malfunctioning.", "Lunch is served at 1200.", "Navigation charts updated.",
        "Security lockdown lifted.", "Unexpected solar winds detected."
    ]

    # Additional line types with simulated metrics and messages
    detailed_log = (
        f"{Fore.GREEN + Style.BRIGHT}[{t}] LOG ENTRY: Temp={Fore.RED if random.random() < 0.3 else Fore.GREEN}{random.uniform(-80, 120):.1f}C{Fore.GREEN + Style.BRIGHT}, "
        f"Radiation={Fore.RED if random.random() < 0.3 else Fore.GREEN}{random.uniform(0.1, 5.0):.2f} mSv{Fore.GREEN + Style.BRIGHT}, "
        f"Coords=({random.uniform(-1000, 1000):.2f}, {random.uniform(-1000, 1000):.2f}, {random.uniform(-1000, 1000):.2f})"
    )
    incoming_transmission = (
        f"{Fore.CYAN + Style.BRIGHT}[{t}] INCOMING TRANSMISSION: '{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- ', k=20))}...'"
    )
    system_diagnostic = (
        f"{Fore.YELLOW + Style.BRIGHT}[{t}] SYSTEM DIAGNOSTIC: {random.choice(['Power', 'Nav', 'Comm', 'Life Support', 'Sensors'])} at "
        f"{random.randint(70, 100)}%, Status: {random.choice(['OK', 'WARN', 'FAIL'])}"
    )
    environmental_reading = (
        f"{Fore.GREEN + Style.BRIGHT}[{t}] ENVIRONMENTAL: Pressure={random.uniform(0.5, 2.0):.2f} atm, Humidity={random.randint(10, 90)}%, "
        f"Wind Speed={random.uniform(0, 150):.1f} km/h"
    )
    mission_update = (
        f"{Fore.YELLOW + Style.BRIGHT}[{t}] MISSION UPDATE: Task '{random.choice(['Calibrate sensors', 'Deploy beacon', 'Collect samples', 'Repair drone', 'Analyze data'])}' "
        f"scheduled for {random.randint(1,12)}:{random.choice(['00','15','30','45'])} hours."
    )
    encryption_update = (
        f"{Fore.CYAN + Style.BRIGHT}[{t}] ENCRYPTION UPDATE: {random.choice(encryption_events)}"
    )
    # Generate a random SHA256-like string
    def random_sha256():
        hex_chars = '0123456789abcdef'
        return ''.join(random.choices(hex_chars, k=64))

    # Simulate a full encryption event with context and chunked hash
    def encryption_hash_event():
        # Pick a context header
        context_headers = [
            "SECURE PAYLOAD SIGNATURE",
            "BLOCKCHAIN HASH",
            "ENCRYPTED PAYLOAD HASH",
            "SIGNATURE VERIFICATION",
            "TRANSACTION HASH",
            "MESSAGE DIGEST"
        ]
        header = random.choice(context_headers)
        # The hash
        hashval = random_sha256()
        # Break hash into 3-5 random chunks
        chunk_sizes = []
        n_chunks = random.choice([3, 4, 5])
        left = 64
        for i in range(n_chunks-1):
            size = random.randint(10, max(12, 64//n_chunks))
            chunk_sizes.append(size)
            left -= size
        chunk_sizes.append(left)
        # Offsets for slicing
        offsets = []
        acc = 0
        for s in chunk_sizes:
            offsets.append((acc, acc+s))
            acc += s
        # Color for hash: mostly cyan, but can be green
        hash_color = Fore.CYAN + Style.BRIGHT if random.random() < 0.8 else Fore.GREEN + Style.BRIGHT
        # Verification status
        status_options = [
            (Fore.GREEN + Style.BRIGHT + "VERIFIED", 0.82),
            (Fore.RED + Style.BRIGHT + "MISMATCH", 0.10),
            (Fore.YELLOW + Style.BRIGHT + "CHECKING", 0.08)
        ]
        r = random.random()
        if r < status_options[0][1]:
            vstatus = status_options[0][0]
        elif r < status_options[0][1] + status_options[1][1]:
            vstatus = status_options[1][0]
        else:
            vstatus = status_options[2][0]
        # Compose lines
        lines = []
        lines.append(f"{hash_color}[{t}] {header}:")
        for i, (start, end) in enumerate(offsets):
            chunk = hashval[start:end]
            # Show chunk index for style
            lines.append(f"{hash_color}    HASH[{i+1}/{n_chunks}]: {chunk}")
        # Add verification status line
        lines.append(f"{hash_color}    STATUS: {vstatus}")
        return lines

    encryption_hash_line = encryption_hash_event()

    # Multi-line message chance
    multi_line_chance = 0.05
    if random.random() < multi_line_chance:
        header = f"{Fore.GREEN + Style.BRIGHT}[{t}] SYSTEM REPORT: Detailed status for {source}"
        details = [
            f"{Fore.RED if random.random() < 0.3 else Fore.GREEN}    - Power levels stable at {random.randint(80, 100)}%",
            f"{Fore.RED if random.random() < 0.3 else Fore.GREEN}    - Temperature nominal at {random.uniform(15, 25):.1f}C",
            f"{Fore.RED if random.random() < 0.3 else Fore.GREEN}    - Radiation within safe limits ({random.uniform(0.1, 1.0):.2f} mSv)",
            f"{Fore.RED if random.random() < 0.3 else Fore.GREEN}    - Communications link: {random.choice(['Strong', 'Weak', 'Intermittent'])}",
            f"{Fore.RED if random.random() < 0.3 else Fore.GREEN}    - Next maintenance window in {random.randint(2, 24)} hours"
        ]
        return [header] + details

    # Graph display chance
    graph_chance = 0.05
    if random.random() < graph_chance:
        graph_lines = generate_random_graph()
        delim = Fore.GREEN + Style.BRIGHT + "==================== GRAPH START ===================="
        delim_end = Fore.GREEN + Style.BRIGHT + "==================== GRAPH END ======================"
        # List of reasons for displaying the graph
        graph_reasons = [
            "ANOMALY DETECTED",
            "NEW DATA INGESTED",
            "SCHEDULED ANALYSIS",
            "OPERATOR REQUEST",
            "AUTOMATED DIAGNOSTIC",
            "PERFORMANCE REVIEW"
        ]
        reason = random.choice(graph_reasons)
        header_line = f"{Fore.GREEN + Style.BRIGHT}{reason} @ {t}"
        # Prepend header line before graph delimiter
        return [header_line, delim] + graph_lines + [delim_end]

    # Solar system map chance (3%)
    if random.random() < 0.03:
        delim = Fore.GREEN + Style.BRIGHT + "==================== STAR SYSTEM MAP START ===================="
        delim_end = Fore.GREEN + Style.BRIGHT + "==================== STAR SYSTEM MAP END ======================"
        header_msg = Fore.GREEN + Style.BRIGHT + "[t] STAR SYSTEM SCAN: Orbital layout detected"
        map_lines = generate_solar_system_map()
        return [delim, header_msg] + map_lines + [delim_end]

    # Crew chat line with rank, name, and location
    crew_ranks = ["Commander", "Engineer", "Pilot", "Navigator", "Technician", "Medic", "Security Officer", "Specialist", "AI", "Researcher"]
    # Pick a crew entity (prefer human/AI names from entities list)
    crew_entities = [
        "Jax", "Lira", "Voss", "Tali", "Ryn", "Sera", "Dex", "Zed", "Mina", "Halv", "Varn", "Zhen"
    ]
    crew_entity = random.choice(crew_entities)
    crew_rank = random.choice(crew_ranks)
    crew_location = random.choice(locations)
    crew_msg = random.choice(crew_chat_msgs)
    crew_chat_line = f"{color}[{t}] CREW CHAT: [{crew_location}] {crew_rank} {crew_entity}: \"{crew_msg}\""

    line_types = [
        f"{color}[{t}] [{channel}] {source} @ {location}: {evt}",
        f"{color}[{t}] SYSTEM STATUS: {source} -> {st}",
        f"{color}[{t}] TRANSMISSION: {source} reports '{evt}'",
        f"{color}[{t}] SENSOR {random.randint(101,999)}-{random.choice(['A','B','C'])}: {evt} near {location}",
        f"{color}[{t}] --- DATA STREAM [{channel}] ---",
        crew_chat_line,
        detailed_log,
        incoming_transmission,
        system_diagnostic,
        environmental_reading,
        mission_update,
        encryption_update,
        encryption_hash_line
    ]

    # Critical messages appear rarely, with blinking effect simulated by surrounding with !!!
    if random.random() < 0.1:
        alert_text = f"{evt.upper()} in {location}!"
        if random.random() < 0.5:
            alert_text = f"!!! {alert_text} !!!"
        return f"{critical_color}[{t}] ALERT: {alert_text}"

    chosen = random.choice(line_types)
    return chosen

# --- Slow printer ---
def slow_print(text, delay=0.0015):
    if isinstance(text, list):
        for line in text:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            print()
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

if __name__ == "__main__":
    print(Fore.GREEN + Style.BRIGHT + "Booting Remote Outpost Terminal...\n")
    time.sleep(2)

    while True:
        line = fake_terminal_line()
        slow_print(line, delay=0.0015)
        time.sleep(random.uniform(0.3, 1.8))  # varied rhythm