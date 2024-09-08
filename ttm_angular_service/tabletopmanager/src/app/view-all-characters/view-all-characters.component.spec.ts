import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewAllCharactersComponent } from './view-all-characters.component';

describe('ViewAllCharactersComponent', () => {
  let component: ViewAllCharactersComponent;
  let fixture: ComponentFixture<ViewAllCharactersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ViewAllCharactersComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ViewAllCharactersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
