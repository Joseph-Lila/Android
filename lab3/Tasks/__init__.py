from kivy.factory import Factory


Factory.register('TrainWidget', module='Controllers.TrainController')
Factory.register('FirstTask', module='Tasks.FirstTask')
Factory.register('SecondTask', module='Tasks.SecondTask')
Factory.register('ThirdTask', module='Tasks.ThirdTask')
Factory.register('BusesList', module='Tasks.BusesList')
Factory.register('AddBus', module='Tasks.AddBus')
Factory.register('Task3TipA', module='Tasks.Task3TipA')
Factory.register('Task3TipB', module='Tasks.Task3TipB')
Factory.register('Task3TipC', module='Tasks.Task3TipC')
Factory.register('RemoveBus', module='Tasks.RemoveBus')
Factory.register('ScreenMaster', module='Tasks.ScreenMaster')

