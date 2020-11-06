import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddAssetDialogComponent } from './add-asset-dialog.component';

describe('AddAssetDialogComponent', () => {
  let component: AddAssetDialogComponent;
  let fixture: ComponentFixture<AddAssetDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddAssetDialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddAssetDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
