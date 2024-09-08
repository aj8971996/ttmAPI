import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddToCharactersComponent } from './add-to-characters.component';

describe('AddToCharactersComponent', () => {
  let component: AddToCharactersComponent;
  let fixture: ComponentFixture<AddToCharactersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddToCharactersComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddToCharactersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
