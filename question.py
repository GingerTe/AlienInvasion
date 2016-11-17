import pygame


class Question:
    def __init__(self, screen):
        """Initialize question attrs"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set button size and params
        self.height = 50
        self.bg_color = (0, 150, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.msg = "Enter your name"
        self.max_answer_len = 10

        self.input = []
        self.answer = None
        self.format_sting()

    def format_sting(self):
        self.full_text = "{}: {}".format(self.msg, "".join(self.input))
        self.width = 20 * len(self.full_text)
        # Create rect object of button and align button in the center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

    def prep_msg(self):
        self.format_sting()
        """Convert msg to rectangle and align text"""
        self.msg_image = self.font.render(self.full_text, True, self.text_color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def ask_question(self):
        """"ask(screen, question) -> answer"""
        pygame.font.init()
        self.draw_question()
        self.input_mode = True

    def draw_question(self):
        self.prep_msg()
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
