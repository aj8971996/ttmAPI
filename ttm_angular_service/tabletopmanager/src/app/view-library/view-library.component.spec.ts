import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewLibraryComponent } from './view-library.component';

describe('ViewLibraryComponent', () => {
  let component: ViewLibraryComponent;
  let fixture: ComponentFixture<ViewLibraryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ViewLibraryComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ViewLibraryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
