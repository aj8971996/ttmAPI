import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewSharedComponent } from './view-shared.component';

describe('ViewSharedComponent', () => {
  let component: ViewSharedComponent;
  let fixture: ComponentFixture<ViewSharedComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ViewSharedComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ViewSharedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
