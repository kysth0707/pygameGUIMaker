import pygame
from Colors import Colors

class PygameGUIMaker(Colors):
	ScreenWidth = None
	ScreenHeight = None
	Title = None

	screen = None
	clock = None

	Run = False

	def __init__(self, Width, Height, SelectorWidth, Title) -> None:
		pygame.init()

		self.SelectorWidth = SelectorWidth
		self.ScreenWidth = Width + self.SelectorWidth
		self.ScreenHeight = Height
		self.screen = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight), pygame.RESIZABLE)
		pygame.display.set_caption(Title)

		self.clock = pygame.time.Clock()
		self.Run = True

	def IsAlive(self):
		return self.Run

	def OnVideoResize(self):
		CurrentSize = pygame.display.get_surface().get_size()
		if self.ScreenWidth != CurrentSize[0]:
			# Width Changed
			pass
		elif self.ScreenHeight != CurrentSize[1]:
			# Height Changed
			pass
		elif self.ScreenWidth != CurrentSize[0] and self.ScreenHeight != CurrentSize[1]:
			# Width / Height Changed
			pass

		self.ScreenWidth, self.ScreenHeight = CurrentSize


	def Update(self):
		self.screen.fill(super().SimulationBackground)
		pygame.draw.rect(self.screen, super().SelectorBackground, [self.ScreenWidth - self.SelectorWidth, 0, self.SelectorWidth, self.ScreenHeight])

		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.Run = False
				pygame.quit()

			elif event.type == pygame.VIDEORESIZE:
				self.OnVideoResize()
		
		self.clock.tick(60)



GUI = PygameGUIMaker(700, 700, 200, "ㅎㅇ")

while True:
	if not GUI.IsAlive():
		break
	GUI.Update()