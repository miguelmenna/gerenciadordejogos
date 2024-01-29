class Player:
    def __init__(self, name):
        self.name = name

class EventNode:
    def __init__(self, event_type, player, time):
        self.event_type = event_type
        self.player = player
        self.time = time
        self.next = None


class EventLog:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_event(self, event_type, player, time):
        new_event = EventNode(event_type, player, time)
        if self.head is None:
            self.head = new_event
        else:
            self.tail.next = new_event
        self.tail = new_event

    def display_events(self):
        current = self.head
        while current:
            print(f"Time: {current.time}, Player: {current.player.name}, Event: {current.event_type}")
            current = current.next


class SubstitutionQueue:
    def __init__(self):
        self.queue = []

    def add_substitution(self, player_out, player_in):
        self.queue.append((player_out, player_in))

    def process_substitution(self):
        if self.queue:
            player_out, player_in = self.queue.pop(0)
            print(f"Substitution: {player_out.name} out, {player_in.name} in")
            return player_out, player_in
        else:
            print("No substitutions in queue.")
            return None, None


class PlayerStats:
    def __init__(self):
        self.stack = []

    def add_stat(self, player, stat_type):
        self.stack.append((player, stat_type))

    def undo_last_stat(self):
        if self.stack:
            player, stat_type = self.stack.pop()
            print(f"Undo last stat for {player.name}: {stat_type}")
            return player, stat_type
        else:
            print("No stats to undo.")
            return None, None


# Exemplo de uso
player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")
player4 = Player("Player 4")

event_log = EventLog()
substitution_queue = SubstitutionQueue()
player_stats = PlayerStats()

# Simulando eventos durante o jogo
event_log.add_event("Scored", player1, "10:30")
event_log.add_event("Foul", player2, "10:00")
event_log.add_event("Assist", player3, "09:45")

substitution_queue.add_substitution(player2, player4)
substitution_queue.add_substitution(player1, player3)

player_stats.add_stat(player1, "2-pointer")
player_stats.add_stat(player3, "assist")
player_stats.add_stat(player2, "foul")

# Exibindo eventos, processando substituições e estatísticas
print("Event Log:")
event_log.display_events()

print("\nProcessing Substitutions:")
substitution_queue.process_substitution()
substitution_queue.process_substitution()
substitution_queue.process_substitution()

print("\nUndoing Last Stat:")
player_stats.undo_last_stat()
player_stats.undo_last_stat()
player_stats.undo_last_stat()
player_stats.undo_last_stat()
