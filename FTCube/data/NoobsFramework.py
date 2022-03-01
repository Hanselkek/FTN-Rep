import pygame

# Found Noobs
FoundNoobs = 0
RecentNoob = "None"
# Main Functions
# Updated, Classes
class update:
    def update_ui(self, value, noobFound):
        global FoundNoobs
        global RecentNoob

        self.noob = noobFound
        self.val = value

        RecentNoob = self.noob
        FoundNoobs += self.val
class show:
    def show_ui(self):
        self.text = pygame.font.SysFont('system', 28)
        self.render = self.text.render("Found Noobs: " + str(FoundNoobs), True, (165, 255, 255))

        return self.render
class showRec:
    def showRecent(self):
        self.recent = pygame.font.SysFont('system', 22)
        self.render = self.recent.render("Recent Noob: " + RecentNoob, True, (165, 255, 255))
        
        return self.render
class showKeys:
    def option(self, x, y, obj, screen):

        screen.blit(obj, (x, y))

    def create(self, wantedString, fontSize):
            self.wanted = pygame.font.SysFont('system', fontSize)
            self.renderedWanted = self.wanted.render(wantedString, True, (165, 255, 255))

            return self.renderedWanted