import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewPlayerCharactersComponent } from './view-player-characters.component';

describe('ViewPlayerCharactersComponent', () => {
  let component: ViewPlayerCharactersComponent;
  let fixture: ComponentFixture<ViewPlayerCharactersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ViewPlayerCharactersComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ViewPlayerCharactersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
