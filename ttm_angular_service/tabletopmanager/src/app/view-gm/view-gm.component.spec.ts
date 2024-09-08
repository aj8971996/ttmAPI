import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewGmComponent } from './view-gm.component';

describe('ViewGmComponent', () => {
  let component: ViewGmComponent;
  let fixture: ComponentFixture<ViewGmComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ViewGmComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ViewGmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
